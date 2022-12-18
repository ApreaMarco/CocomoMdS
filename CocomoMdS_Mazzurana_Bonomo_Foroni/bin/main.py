from sys import version
from os import path
from time import time
import keywords as keys

#Global Variables
_author_ = ["Riccardo Mazzurana", "Pietro Foroni", "Giovanni Bonomo"]
_copyright_ = "Copyright 2022"
_credits_ = ["Riccardo Mazzurana", "Pietro Foroni", "Giovanni Bonomo"]
_license_ = "GPL"
_version_ = "1.0.0"
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

    #Get language used
    percentage = keys.keywordsCount(fileContent)
    prevalentLang = lang = max(percentage, key=percentage.get)

    return percentage, prevalentLang

def getExtension(filename):
    """
    Returns the extension of a given filename

        Parameters:
            filename (str): name of the file

        Returns:
            ext (str): extension
    """

    #Get Extension
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

    if not path.exists(filePath):
        if boold:
            print("File does not exists")
        return False
    elif not path.isfile(filePath):
        if boold:
            print("Path is not a file")
        return False
    else:
        return True

def main():
    #File input
    if boold:
        print("Main")
        filename = "../test/test.py"
    else:
        filename = input("Insert filename: ")
        while not checkFile(filename):
            filename = input("Error! Re-Insert filename: ")

    lang, prevalentLang = getLanguages(filename)
    ext = getExtension(filename)

    #Output
    print()
    for key in lang.keys():
        print(f"Language: {key} -> {lang[key]}%")

    print(f"\nPrevalent Language: {prevalentLang}")
    print(f"File extension: {ext}")

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
