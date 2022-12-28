from os import path, listdir
import re

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

LANGS = []
files = listdir("../keywords")
for name in files:
    name = name[0:-4]
    LANGS.append(name)

KEYWORDS = {}
for name in LANGS:
    path = "../keywords/" + name + ".txt"
    with open(path, "rt") as f:
        temp_list = []
        for word in f:
            temp_list.append(word.strip())
        KEYWORDS[name] = temp_list


def keywordsCount(text):
    """
    Calculates the percentages of the languages based on how many times some keyword of each language are in the text.

        Parameters:
            text (str): text which keywords are extracted from

        Returns:
            percentage (dict): python dictionary with the calculated percentages of each language
    """

    splitted = re.split("\n| |[(]|[{]|=|[+]|-|[*]|/|;", text)
    counters = dict.fromkeys(LANGS, 0)
    percentage = dict.fromkeys(LANGS, 0)
    sum = 0

    for lang in LANGS:
        for keyword in KEYWORDS[lang]:
            counters[lang] += splitted.count(keyword)
            sum += splitted.count(keyword)

    for lang in LANGS:
        percentage[lang] = round(
            ((counters[lang] * 100) / sum), 2)  # type: ignore

    return percentage
