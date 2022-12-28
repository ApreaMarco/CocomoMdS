import re
from os import path

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

def cocomo(path, dif):
    file = open(path, "r")
    content = file.readlines()

    LOC = 0

    difficulty = ""
    developmentTime = 0
    monthsMan = 0

    easyLOC = [2.4, 1.05, 2.5, 0.38]
    intermediateLOC = [3, 1.12, 2.5, 0.35]
    complexLOC = [3.6, 1.12, 2.5, 0.32]

    for line in content:
        if (re.search("[a-zA-Z]", line) or re.search ("\n", line)):
            LOC += 1
    file.close()

    if (dif == 1):
        difficulty = "easy"
        a = easyLOC[0]
        b = easyLOC[1]
        c = easyLOC[2]
        d = easyLOC[3]

    elif (dif == 2):
        difficulty = "intermediate"
        a = intermediateLOC[0]
        b = intermediateLOC[1]
        c = intermediateLOC[2]
        d = intermediateLOC[3]

    else:
        difficulty = "complex"
        a = complexLOC[0]
        b = complexLOC[1]
        c = complexLOC[2]
        d = complexLOC[3]

    monthsMan = a * ((LOC / 1000)**b)
    developmentTime = c * (monthsMan ** d)

    result = "".join([f"number of lines of code: {str(LOC)}\ndifficulty: {str(difficulty)}\nmonths man: {str(round(monthsMan, 2))}\ndevelopment time: {str(round(developmentTime, 2))}"])
    return result
