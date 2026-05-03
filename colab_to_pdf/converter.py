import os
import asyncio
import tempfile
from pathlib import Path
import nbformat
from nbconvert import HTMLExporter
from playwright.async_api import async_playwright

class ColabToPDFConverter:
    def __init__(self, input_path):
        self.input_path = Path(input_path)
        self.output_path = self.input_path.with_suffix('.pdf')

    async def _install_browser(self):
        """Ensures Chromium is installed for Playwright."""
        print("Checking for Chromium...")
        import subprocess
        import sys
        try:
            # This is a simple way to trigger playwright install
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        except Exception as e:
            print(f"Error installing browser: {e}")

    async def convert(self):
        # 1. HTML Conversion using nbconvert
        print(f"Converting {self.input_path} to HTML...")
        with open(self.input_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        html_exporter = HTMLExporter()
        # We can customize the template if needed, but standard is fine as we'll override styles
        (body, resources) = html_exporter.from_notebook_node(nb)

        # 2. Setup Playwright and Render
        async with async_playwright() as p:
            # Try to launch, if it fails, try to install
            try:
                browser = await p.chromium.launch()
            except Exception:
                await self._install_browser()
                browser = await p.chromium.launch()

            page = await browser.new_page()

            # Create a temporary HTML file to load into Playwright
            with tempfile.NamedTemporaryFile(suffix='.html', delete=False, mode='w', encoding='utf-8') as tmp_html:
                tmp_html.write(body)
                tmp_html_path = tmp_html.name

            try:
                # Load the HTML
                await page.goto(f"file://{os.path.abspath(tmp_html_path)}")

                # 3. Style Overrides (Crucial)
                print("Applying style overrides...")
                # Trick the notebook into rendering full digital colors
                await page.emulate_media(media="screen")

                # Inject CSS to bypass print greyscale
                css_override = """
                @media print {
                    span, code, pre {
                        color: inherit !important;
                        -webkit-print-color-adjust: exact !important;
                        print-color-adjust: exact !important;
                    }
                    .nb-output, .nb-input {
                        page-break-inside: avoid;
                    }
                }
                """
                await page.add_style_tag(content=css_override)

                # 4. PDF Generation
                print(f"Generating PDF: {self.output_path}")
                await page.pdf(
                    path=str(self.output_path),
                    format="A4",
                    print_background=True,
                    margin={"top": "1cm", "right": "1cm", "bottom": "1cm", "left": "1cm"}
                )
            finally:
                await browser.close()
                if os.path.exists(tmp_html_path):
                    os.remove(tmp_html_path)

        print("Conversion complete!")

async def run_conversion(input_path):
    converter = ColabToPDFConverter(input_path)
    await converter.convert()
