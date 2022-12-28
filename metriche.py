import os
import re

def loc(filePath):
    file = open(filePath, "r")
    lines = 0
    for line in file:
        lines += 1
    file.close
    return lines

def cloc(filePath):
    file = open(filePath, "r")
    lines = 0
    for line in file:
        line = str(line.strip)
        if(line.startswith("#")):
            lines += 1
    file.close
    return lines

def nloc(filePath):
    file = open(filePath, "r")
    lines = 0
    for line in file:
        line = str(line.strip)
        if (line.startswith("#")):
            lines += 1
    file.close
    return lines

def ciclomatico(filePath):
    file = open(filePath, "r")
    num = 1
    for line in file:
        if(re.search("^\s*if ", line)) or (re.search("^\s*if\s*(.+)", line)):
                num += 1
        if(re.search("^\s*for ", line)) or (re.search("^\s*for\s*(.+)", line)):
                num += 1
        if(re.search("^\s*while ", line)) or (re.search("^\s*while\s*(.+)", line)):
                num += 1
    file.close
    return num

def cocomoBase(filePath):
    appTypes = [
    [3.20, 1.05, 2.50, 0.38],
    [3.00, 1.12, 2.50, 0.35],
    [2.80, 1.20, 2.50, 0.32]
    ]
    type = int(input("Tipo applicazione (0- semplice, 1- intermedia, 2- complessa): "))
    while(type < 0 or type > 2):
        type = int(input("Tipo applicazione (0- semplice, 1- intermedia, 2- complessa): "))

    if(type == 0):
        a = appTypes[0][0]
        b = appTypes[0][1]
        c = appTypes[0][2]
        d = appTypes[0][3]
    elif(type == 1):
        a = appTypes[1][0]
        b = appTypes[1][1]
        c = appTypes[1][2]
        d = appTypes[1][3]
    else:
        a = appTypes[2][0]
        b = appTypes[2][1]
        c = appTypes[2][2]
        d = appTypes[2][3]

    s = nloc(filePath)

    s /= 1000
    m = a * (s**b)
    #td = c * (m**d)
    return m


def cocomoIntermedio(filePath):
    appTypes = [
    [3.20, 1.05, 2.50, 0.38],
    [3.00, 1.12, 2.50, 0.35],
    [2.80, 1.20, 2.50, 0.32]
    ]

    type = int(input("Tipo applicazione (0- semplice, 1- intermedia, 2- complessa): "))
    while(type < 0 or type > 2):
        type = int(input("Tipo applicazione (0- semplice, 1- intermedia, 2- complessa): "))

    if(type == 0):
        a = appTypes[0][0]
        b = appTypes[0][1]
        c = appTypes[0][2]
        d = appTypes[0][3]
    elif(type == 1):
        a = appTypes[1][0]
        b = appTypes[1][1]
        c = appTypes[1][2]
        d = appTypes[1][3]
    else:
        a = appTypes[2][0]
        b = appTypes[2][1]
        c = appTypes[2][2]
        d = appTypes[2][3]

    s = nloc(filePath)
    s /= 1000

    costDrivers = [
        [1.46, 1.19, 1.00, 0.86, 0.71, 1.00],
        [1.29, 1.13, 1.00, 0.91, 0.86, 1.00],
        [0.70, 0.85, 1.00, 1.15, 1.30, 1.65],
        [1.00, 0.94, 1.00, 1.08, 1.16, 1.00],
        [1.14, 1.07, 1.00, 0.95, 1.00, 1.00],
        [1.24, 1.10, 1.00, 0.91, 0.82, 1.00],
        [0.75, 1.17, 1.00, 0.86, 0.70, 1.00],
        [1.23, 0.88, 1.00, 1.15, 1.40, 1.00],
        [1.23, 1.08, 1.00, 1.04, 1.10, 1.00],
        [1.00, 1.00, 1.00, 1.06, 1.21, 1.56],
        [1.00, 1.00, 1.00, 1.11, 1.30, 1.66],
        [1.24, 1.10, 1.00, 0.91, 0.83, 1.00],
        [1.00, 0.87, 1.00, 1.07, 1.15, 1.00],
        [1.21, 1.10, 1.00, 0.90, 1.00, 1.00],
        [1.00, 0.87, 1.00, 1.15, 1.30, 1.00]
    ]

    costDriversNames = ["acap", "aexp", "cplx", "data" ,"lexp", "mcdp", "pcap", "rely", "sced", "stor", "time", "tool", "turn", "vexp","virt"]
    eaf = 1
    for i in range(0, len(costDrivers)):
        value = int(input(costDriversNames[i] + ": "))
        while(value < 0 or value > 5):
            print("valore non valido")
            value = int(input(costDriversNames[i] + ": "))
        else:
            eaf *= costDrivers[i][value]

    mnom = a * (s**b) * eaf
    return mnom
    