__author__ = ["Aprea Marco"]
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = ["Aprea Marco"]
__email__ = ["marco.aprea@marconiverona.edu.it"]

from pathlib import Path
from fileToText import plainText
from languageDetection import getRecognizedLanguage as grl1
from languageDetection import getRecognizableLanguage as grl2
from codeMetrics import getAllMetrics as gam
from codeMetrics import getAllExtensions as gae1
from languageExtensions import getAllExtension as gae2


def main():
    absPath = "/home/apream/CodiumProjects/C++/"
    fileName = "classeStudente.cpp"
    absPathFile = Path(absPath + fileName)

    text = ""

    if Path.is_file(absPathFile):
        text = plainText(absPathFile)

    if len(text) > 0:
        print(text)
        print(grl1(text))  # Fetch recognized language and his probability by guesslang
        print(grl2())  # Fetch all regnizable language by guesslang
        print(gam(fileName, text))  # Fetch all metrics of provided code source by lizard
        print(gae1())  # Fetch some extensions of languages analizable by lizard
        print(gae2())  # Fetch all extensions of languages knowed by linguist


if __name__ == "__main__":
    main()
