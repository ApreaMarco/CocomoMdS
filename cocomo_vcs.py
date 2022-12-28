import os
import re
from keywords import keywords
import metriche


def getInputFiles():
    inputPath = input("Inserire percorso file: ")
    while not(os.path.exists(inputPath)):
        inputPath = input("Inserire percorso file: ")
    files = []
    if(os.path.isdir(inputPath)):
        for file in os.listdir(inputPath):
            files.append(inputPath + "/" + file)
    else:
        files.append(inputPath)
    return files


def calculate(filePath, outputFile):
    print("-----------------------------------------------------------------------------------")
    print("0-LOC 1-CLOC 2-NLOC 3-Num Ciclomatico 4-COCOMO base 5-COCOMO intermedio")
    proceed = True
    outputFile.write("File: " + filePath + "\n")
    while proceed:
        mode = int(input("Tipo di calcolo file " + filePath + ": "))
        while(mode < 0 or mode > 5):
            mode = int(input("Tipo di calcolo: "))
        if(mode == 0):
            result = metriche.loc(filePath)
            outputFile.write("LOC: " + str(result) + "\n")
        elif(mode == 1):
            result = metriche.cloc(filePath)
            outputFile.write("CLOC: " + str(result)  + "\n")
        elif(mode == 2):
            result = metriche.nloc(filePath)
            outputFile.write("NLOC: " + str(result)  + "\n")
        elif(mode == 3):
            result = metriche.ciclomatico(filePath)
            outputFile.write("numero ciclomatico: " + str(result)  + "\n")
        elif(mode == 4):
            result = metriche.cocomoBase(filePath)
            outputFile.write("cocomo base: " + str(result)  + "\n")
        else:
            result = metriche.cocomoIntermedio(filePath)
            outputFile.write("cocomo intermedio: " + str(result)  + "\n")
        
        ask = input("Effettuare altri calcoli sul file " + filePath + "? (y/n): ")
        if(ask == "n"):
            proceed = False
        elif(ask == "y"):
            proceed = True
        else:
            ask = input("Effettuare altri calcoli sul file " + filePath + "? (y/n): ")


def getProgrammingLanguage(inputPath, outputFile):
    outputFile.write("File: " + inputPath + "\n")
    languages = keywords.keys()
    inputFile = open(inputPath, "r")
    lines = inputFile.readlines()
    totWords = 0

    for key in languages:
        words =  0
        percentage = 0
        for line in lines:
            totWords += len(line.split())
            for i in range(0, len(keywords[key])):
                if re.search("^.+ " + keywords[key][i] + " .+$", line) or re.search("^.+ " + keywords[key][i] + " *\(.+$", line) or re.search("^\s*" + keywords[key][i] + " *\(.+$", line) or re.search("^\s*" + keywords[key][i] + " *\(.+$", line):
                    if not (line.startswith(keywords[key][0])):
                        words += 1
        percentage = round((words * 100) / totWords, 2)
        outputFile.write(key + ": " + str(percentage) + "%\n")

    inputFile.close()


def main():
    outputFile = open("metriche.txt", "w")
    inputFiles = getInputFiles()

    for file in inputFiles:
        outputFile.write("Percorso file o cartella: " + file + "\n")
        getProgrammingLanguage(file, outputFile)
        calculate(file, outputFile)
        outputFile.write("\n---------------------------------------------------------\n")

    outputFile.close


if __name__ == "__main__" :
    main()
