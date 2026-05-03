from setuptools import setup, find_packages

setup(
    name="colabToPDF",
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
            "colabToPDF=colab_to_pdf.cli:main",
        ],
    },
    author="Antigravity",
    description="A tool to convert Google Colab notebooks to PDF with true colors.",
)
