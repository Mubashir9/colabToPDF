from setuptools import setup, find_packages

setup(
    name="truecolor-colab-pdf",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "playwright",
        "nbconvert",
        "nbformat",
        "ipython",
    ],
    entry_points={
        "console_scripts": [
            "truecolor-export=truecolor_pdf.cli:main",
        ],
    },
    author="Antigravity",
    description="A tool to convert Google Colab notebooks to PDF with true colors.",
)
