## Project Specification: "TrueColor-Colab-PDF"

### Objective
Build a Python-based command-line tool that converts a Google Colab `.ipynb` file into a PDF while strictly preserving the "Screen" colors (syntax highlighting, bold text, and backgrounds) and preventing the "greyed-out" effect caused by standard print media queries.

### 1. Project Structure
The project should be structured as a standard Python package:
*   `setup.py`: To make the tool installable via `pip`.
*   `truecolor_pdf/`: The main package folder.
    *   `__init__.py`
    *   `converter.py`: The core logic using Playwright.
    *   `cli.py`: Entry point for the terminal command.
*   `requirements.txt`: Including `playwright`, `nbconvert`, and `nbformat`.

### 2. Core Technical Requirements
The conversion pipeline must follow these specific steps:
1.  **HTML Conversion:** Use `nbconvert` to convert the `.ipynb` to a temporary HTML file.
2.  **Headless Browser Execution:** Use **Playwright (Chromium)** to open that HTML file.
3.  **Style Overrides (Crucial):**
    *   Inject a CSS block to force `color: inherit !important` on all `span`, `code`, and `pre` tags to bypass "Print" greyscale styling.
    *   Use `page.emulate_media(media="screen")` to trick the notebook into rendering its full digital colors.
4.  **PDF Generation:** Use `page.pdf()` with `print_background=True` enabled.

### 3. Execution Flow (The "One-Liner")
The user should be able to run this in a Colab cell:
```python
!pip install git+https://github.com/[Username]/TrueColor-Colab-PDF.git
!truecolor-export my_notebook.ipynb
```

### 4. Implementation Details for the AI (Antigravity)
> "Please write the code for `converter.py` using `asyncio` for Playwright. Ensure the tool automatically handles the installation of the Chromium browser if it isn't found. The CLI should accept the input filename as an argument and output a PDF with the same name."

---

