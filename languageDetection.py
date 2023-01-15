from guesslang import Guess


def languageDetection(text=None, resultFilter=None, itemSort=None, descendingSort=None):
    retVal = []

    if text is None:  # None-> getting list of knowed language
        text = ""

    if itemSort is None or itemSort != 0:  # 0-> language, 1 -> percentuage
        itemSort = 1

    if descendingSort is None:
        descendingSort = True

    guess = Guess().probabilities(text)
    guess.sort(key=lambda i: i[itemSort], reverse=descendingSort)

    if resultFilter is None or resultFilter > len(guess):
        resultFilter = len(guess)

    for item in range(resultFilter):
        retVal.append(guess[item])

    return retVal


def getRecognizableLanguage():
    retVal = []

    languages = languageDetection(None, None, 0, False)

    for language in languages:
        retVal.append(language[0])

    return retVal


def getRecognizedLanguage(text):
    return languageDetection(text, 1)
