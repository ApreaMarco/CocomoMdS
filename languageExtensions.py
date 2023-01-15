import requests
import yaml


def getAllExtension():
    retVal = {}
    key = 'extensions'

    a = requests.get("https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml")
    y = yaml.safe_load(a.text)

    for lang in y.keys():
        if key in y[lang]:
            retVal[lang] = y[lang][key]

    return retVal
