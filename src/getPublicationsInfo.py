import os
import re

TXT_FILES_LOCATION = '../txtFiles'
CSV_LOCATION = '../publicationsData.csv'

__author__ = 'timothy'

pubsLineRegex = re.compile('^(?:\d*\s+)?(?:.*?)\s+(?:(?:\d+ \w{3}(?: \d+)? to )?\d+ \w{3} \d+)?\s+(?:-?\$\d+\.\d{2})?')
quantityRegex = re.compile('^(\d*\s+)?(?:.*?)\s+(?:(?:\d+ \w{3}(?: \d+)? to )?\d+ \w{3} \d+)?\s+(?:-?\$\d+\.\d{2})?')
pubNameRegex = re.compile('^(?:\d*\s+)?(.*?)\s+(?:(?:\d+ \w{3}(?: \d+)? to )?\d+ \w{3} \d+)?\s+(?:-?\$\d+\.\d{2})?')
dateRegex = re.compile('^(?:\d*\s+)?(?:.*?)\s+((?:\d+ \w{3}(?: \d+)? to )?\d+ \w{3} \d+)?\s+(?:-?\$\d+\.\d{2})?')
priceRegex = re.compile('^(?:\d*\s+)?(?:.*?)\s+(?:(?:\d+ \w{3}(?: \d+)? to )?\d+ \w{3} \d+)?\s+(-?\$\d+\.\d{2})?')

def parsePublications(filename, inFP, outFP):
    inFP.readline()
    for line in inFP:
        if line.isspace():
            return
        elif not pubsLineRegex.match(line):
            print("Unable to parse line \"" + line.strip() + "\"")
        else:
            quantity = quantityRegex.findall(line)[0]
            pubName = pubNameRegex.findall(line)[0]
            date = dateRegex.findall(line)[0]
            price = priceRegex.findall(line)[0]

            outFP.write(','.join(map(str, [filename.strip(), quantity, "\"" + pubName.strip() + "\"", date.strip(), price.strip()])) + '\n')


def parseReports():
    outFP = open(CSV_LOCATION, 'w')
    outFP.write(','.join(["Politician", "Quantity", "Publication", "Date", "Price"]) + "\n")

    for filename in os.listdir(TXT_FILES_LOCATION):
        print('Doing ' + filename)
        with open(TXT_FILES_LOCATION + '/' + filename) as fp:
            for line in fp:
                if line.rstrip() == 'Publications':
                    parsePublications(filename, fp, outFP)

    outFP.close()

if __name__ == '__main__':
    parseReports()