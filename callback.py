#!python3

import os
import re
import json

# scripts import on scripts/ directory
import scripts.files_checker as FILES_CHECKER
import scripts.base_COCOMO as BASE_COCOMO

__author__ = ["Rajapaksha Kasun", "Serratore Federico", "Villardi Riccardo"]
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = ["Rajapaksha Kasun",
                  "Serratore Federico", "Villardi Riccardo"]
__email__ = ["19221@studenti.marconiverona.edu.it",
             "19169@studenti.marconiverona.edu.it", "19245@studenti.marconiverona.edu.it"]

# clear terminal
os.system("cls")

MY_PATH = ""    # input path
OUTPUT_FILE = "Analyzer.json"


def fileOutput(filePath, results_dict):
    fullPath = os.path.join(os.path.dirname(__file__), OUTPUT_FILE)
    print(f"---Check file '{OUTPUT_FILE}' existance")
    if (not os.path.exists(fullPath)):
        print("---Create .json file")

        # create and write on .json file
        with open(fullPath, 'w') as json_outputFile:
            json_outputFile.write(json.dumps(results_dict, indent=4))

        print(f"\n---'{OUTPUT_FILE}' succesfully created")
    else:
        output_dict = {}
        print(f"---Check into the file '{OUTPUT_FILE}'")

        with open(fullPath, 'r') as json_outputFile:
            data = json.load(json_outputFile)

        # choose to update or upgrade .json file
        is_updated = False

        # check filePath on .json file
        for i_key in data.keys():
            # find filePath on .json file
            if (not is_updated and filePath == i_key):
                print("\n---File on .json founded")

                if (data[i_key] == results_dict[i_key]):
                    print("---Results are the same, .json didn't edit")
                    return
                else:
                    print("---Update .json file")
                    data[i_key] = results_dict[filePath]
                    is_updated = True

            # recreate .json
            output_dict[i_key] = data[i_key]

        if (not is_updated):
            print("---Add new file to the .json")
            output_dict[filePath] = results_dict[filePath]

        with open(fullPath, 'w', newline="\n") as json_outputFile:
            json_outputFile.write(json.dumps(output_dict, indent=4))

        print(f"\n---'{OUTPUT_FILE}' succesfully modified\n")


def conf_files_to_dict(app):
    print("\n---Extract keywords from .conf files")
    my_dict = {}
    for conf_file in app:
        line = ""
        lang = ""
        with open(conf_file, 'r') as _file:
            for line in _file:
                line = line.strip()

                if "LANG=" in line:
                    lang = line.split("=")[1]
                    my_dict[lang] = ""
                elif "KEYWORDS=" in line:
                    my_dict[lang] = line.split("=")[1].strip().split(",")
                else:
                    my_dict[lang] += line.strip().split(",")

            print(f"---{conf_file} file elaborated")

    print("---Extraction completed\n")
    return my_dict


def count_keywords(string, app):
    conf_dict = conf_files_to_dict(app)
    counter = dict.fromkeys(list(conf_dict.keys()), 0)
    max_language = ["ling", 0]

    words = string.split()

    print("---Analyzing the program language of the file")
    for ling, keywords in conf_dict.items():
        i_count = 0
        for keyword in keywords:
            i_count += words.count(keyword)

        if (i_count > max_language[1]):
            max_language = [ling, i_count]
        elif (i_count == max_language[1]):
            max_language = ["undefined", i_count]

        counter[ling] = f"{round(i_count/len(words) *100, 2)}%"
    print("---Analyzation completed")

    return counter, max_language[0]


def search_file_type(app):
    ext = os.path.splitext(MY_PATH)[1]

    f = open(MY_PATH)

    keywords_counter, language = count_keywords(f.read(), app)

    total_dict = {}
    total_dict["Software metrics"] = keywords_counter
    total_dict['base COCOMO'] = BASE_COCOMO.calculate_BASE_COCOMO(MY_PATH)
    total_dict["Elaboration"] = {
        "File extension:": ext,
        "Elaborated language:": language,
        "Is analysis correct:": language == ext
    }

    return total_dict


def inputRequest():
    global MY_PATH

    # input file request
    while True:
        MY_PATH = input("---INSERT FILE TO READ:\n").strip()

        # check and remove double quotes in the input
        if ((len(MY_PATH) > 0) and (MY_PATH[0] == '"' or MY_PATH[len(MY_PATH)-1] == '"')):
            MY_PATH = MY_PATH.replace('"', "")

        # quit the loop when file exists and it's a file
        if (os.path.exists(MY_PATH)):
            # check if path is a file
            if (os.path.isfile(MY_PATH)):
                break

            print("---Path selected is a file\n")

        print("---File doesn't exists\n")


def main():
    print("---PROGRAM LANGUAGES ANALYZER---")

    # Check necessary files existance
    FILES_CHECKER.check_files()

    # INPUT
    inputRequest()

    # array of all .conf files
    app = FILES_CHECKER.CONF_FILES

    results_dict = {}
    results_dict[MY_PATH] = search_file_type(app)

    # write output on .json file
    fileOutput(MY_PATH, results_dict)


if __name__ == "__main__":
    main()
