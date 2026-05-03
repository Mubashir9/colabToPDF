# colabToPDF

A Python-based command-line tool designed to convert Google Colab `.ipynb` files into high-fidelity PDFs. It strictly preserves "Screen" colors (syntax highlighting, bold text, and backgrounds) and prevents the "greyed-out" effect caused by standard print media queries.

## 🚀 Features
- **High-Fidelity Colors**: Uses browser rendering to capture syntax highlighting as seen on screen.
- **Screen Emulation**: Bypasses print media queries that often strip colors.
- **Auto-setup**: Automatically installs the required Chromium browser via Playwright.

## 🛠️ Usage in Google Colab

To use this tool directly in a Colab notebook, run the following commands in a cell:

```python
# 1. Install the tool
!pip install git+https://github.com/Mubashir9/colabToPDF.git

# 2. Export your notebook
!truecolor-export my_notebook.ipynb
```

## 💻 Local Installation

You can also use this tool locally:

```bash
git clone https://github.com/Mubashir9/colabToPDF.git
cd colabToPDF
pip install -e .
```

Then run:
```bash
truecolor-export path/to/notebook.ipynb
```

## 📜 How it works
1. **HTML Conversion**: Uses `nbconvert` to generate a base HTML structure.
2. **Browser Rendering**: Launches a headless **Chromium** browser via **Playwright**.
3. **Style Injection**: Inject CSS to force `color: inherit !important` on code spans and emulates `media="screen"`.
4. **PDF Generation**: Prints the page to a PDF with `print_background=True`.

## 📄 License
MIT
