from sys import version
from os import path
from time import time
import keywords as kw
from cocomo import cocomo

_author_ = ["Riccardo Mazzurana", "Pietro Foroni", "Giovanni Bonomo"]
_copyright_ = "Copyright 2022"
_credits_ = ["Riccardo Mazzurana", "Pietro Foroni", "Giovanni Bonomo"]
_license_ = "GPL"
_version_ = "2.0.0"
_maintainer_ = ["Riccardo Mazzurana", "Pietro Foroni", "Giovanni Bonomo"]
_email_ = ["19118@studenti.marconiverona.edu.it", "19039@studenti.marconiverona.edu.it", "19036@studenti.marconiverona.edu.it"]
_status_ = "Development"
boold = False
programname = path.basename(__file__)


def getLanguages(filename):
    """
    Returns programming languages of a given filename

        Parameters:
            filename (str): name of the file

        Returns:
            percentage (str[]): list of languages
            prevalentLang (str): prevalent language used in the given file
    """

    with open(filename, 'r') as f:
        fileContent = f.read()

    percentage = kw.keywordsCount(fileContent)
    prevalentLang = max(percentage, key=percentage.get)  # type: ignore

    return percentage, prevalentLang


def getExtension(filename):
    """
    Returns the extension of a given filename

        Parameters:
            filename (str): name of the file

        Returns:
            ext (str): extension
    """

    ext = path.splitext(filename)[1]

    return ext


def checkFile(filePath):
    """
    Check if path given exists and is a file

        Parameters:
            filePath (str): file path

        Returns:
            bool: true if path exists and is a file, false otherwise
    """

    retValue = False
    if not path.exists(filePath):
        if boold:
            print("file does not exists")
    elif not path.isfile(filePath):
        if boold:
            print("path is not a file")
    else:
        retValue = True
    
    return retValue


def main():
    if boold:
        print("Main")
        filename = "../test/test.py"

    else:
        filename = input("insert filename: ")
        while not checkFile(filename):
            filename = input("error! re-insert filename: ")

    lang, prevalentLang = getLanguages(filename)
    ext = getExtension(filename)

    result = f"Script analysis for {filename}\n"
    for key in lang.keys():
        result += f"\nlanguage: {key} -> {lang[key]}%"

    result += f"\n\nprevalent Language: {prevalentLang}\n"
    result += f"file extension: {ext}\n"
    
    diff = int(input("\ninsert the difficulty for cocomo (1-3): "))
    while diff < 1 or diff > 3:
        diff = int(input("error! re-insert the difficulty for cocomo (1-3): "))

    cocomo_result = cocomo(filename, diff)
    result += f"\ncocomo result: \n{cocomo_result}"

    with open("../result/results.txt", "w") as f:
        f.write(result)


if __name__ == '__main__':
    if boold:
        msg = "".join(["Executing ", programname, " with Python ", version])
        print(msg)

    t1 = time()
    main()
    t2 = time()

    if boold:
        msg = "".join(["Code Executed in ", str(t2 - t1), " seconds"])
        print(msg)
