# Publications Expense Reports

A small project that uses some simple python scripts and the Plopper pdf utilities to download and extract information
about publications listed in the expense reports of Federal Australian MPs during the first half of 2014.

## Usage

The downloadPDFs.py script downloads the pdfs listed in urls.txt file into the pdfs/ directory. It then employs the
pdftotext utility to convert these to txt files, placing these in the txtFiles/ directory.

The getPublicationsInfo.py script reads the txt files in the txtFiles/ directory and outputs a file
publicationsData.csv containing the information.

## Requirements

This project requires Python 3 and the Plopper pdf utilities to be installed and on the path.