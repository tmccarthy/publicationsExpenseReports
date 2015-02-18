__author__ = 'timothy'

from urllib.request import urlretrieve
from subprocess import call
import re

def downloadPDFs():
    filenameExtract = re.compile("^http://www.finance.gov.au/sites/default/files/P34_(.*).pdf")

    with open('../urls.txt') as f:
        for url in f:
            name = filenameExtract.findall(url)[0]
            downloadPDF(url, name)
            convertPDF(name)


def downloadPDF(url, name):
    print('Downloading ' + url + ' to ' + name + '.pdf')
    urlretrieve(url, '../pdfs/' + name + '.pdf')


def convertPDF(name):
    print('Converting ' + name + '.pdf to ' + name + '.txt')
    call(['pdftotext', '-layout', '../pdfs/' + name + '.pdf', '../txtFiles/' + name + '.txt'])


if __name__ == '__main__':
    downloadPDFs()