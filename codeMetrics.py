from lizard import analyze_file as af
from lizard import languages as lang


def getAllMetrics(fileName, text):
    analizedFile = af.analyze_source_code(fileName, text)

    functionList = []

    for function in analizedFile.function_list:
        dictFunction = function.__dict__

        singleFunction = {"functionName": dictFunction["long_name"],
                          "NLOC": dictFunction["nloc"],
                          "CCN": dictFunction["cyclomatic_complexity"],
                          "token": dictFunction["token_count"]}

        functionList.append(singleFunction)

    return {"fileName": fileName, "NLOC": analizedFile.nloc, "CCN": analizedFile.CCN,
            "token": analizedFile.token_count, "numberOfFunctions": len(functionList),
            "allFunctions": functionList}


def getAllExtensions():  # Lizard doesn't provide updated list of extensions that can analize
    retVal = []

    for languages in lang():
        retVal.append(languages.ext)

    return retVal
