"""
Description: Python program that determines the language in which a code file is written and checks
             if it matches its extension.
"""

import os
import re
from collections import Counter
from keywords import LANGS
import cocomo

# Globals
PRODUCTION = True
DEBUG = False


# Functions
def count_keywords(filepath):
    """
    Analyzes a code file and return a dictionary of percentages for the following languages:
    python, java, c, c++, c#, php, javascript, assembly 8086, batch, bash, powershell.

        Parameters:
            filepath (str): Path to the file to analyze

        Returns
            percentages (dict): Dictionary of percentages for every language
    """
    # Open and read the file
    file = open(filepath, 'r')
    content = file.read()
    file.close()

    # Keywords counting
    keywords = re.split("\n| |[(]|[)]|[{]|[}]|=|[+]|-|[*]|/|,|;|[.]|:|<|[$]", content)

    keyword_occurrences = Counter(keywords)  # Group keywords
    keyword_occurrences.pop("")  # Delete empty spaces
    unrecognized_keywords = dict.fromkeys(keyword_occurrences, 0)

    # Count keywords for every language
    counters = dict.fromkeys(LANGS, 0)
    for lang in LANGS:
        for key in keyword_occurrences:
            if key in LANGS[lang]["keywords"]:
                counters[lang] += keyword_occurrences[key]
                unrecognized_keywords[key] += 1

    # Count unrecognized keywords
    counters["unrecognized"] = 0
    for key in unrecognized_keywords:
        if not unrecognized_keywords[key]:
            counters["unrecognized"] += keyword_occurrences[key]

    # Calculate percentages
    tot = sum(keyword_occurrences.values())
    percentages = {lang: (100 * counters[lang] / tot) for lang in counters}

    return percentages


def is_valid(filepath, verbose=False):
    """
    Checks if a path exists and corresponds to a file.

        Parameters:
            filepath (str): Path to the file
            verbose (bool): If true prints error messages

        Returns:
            validity (bool): File validity
    """
    if not os.path.exists(filepath):
        if verbose:
            print("File does not exist.")
        return False
    elif not os.path.isfile(filepath):
        if verbose:
            print("The path entered is not a file.")
        return False
    else:
        return True


def main():
    user_continue = True
    while user_continue:
        # Input file
        if DEBUG:
            filepath = "../test/test.py"
        else:
            filepath = input('Insert file path: ')
            while not is_valid(filepath):
                filepath = input('Error! Reinsert file path: ')

        # Analyze file
        percentages = count_keywords(filepath)

        # Get language and extension
        extension = os.path.splitext(filepath)[1]

        lang_percentages = {key: percentages[key] for key in percentages if key != "unrecognized"}  # Excl. unrecognized
        max_percentage = max(lang_percentages.values())  # Find the highest percentage

        languages = None
        if max_percentage > 0:  # If there is at least one language with percentage greater than 0
            # Languages with the highest percentage
            languages = [lang for lang in lang_percentages if lang_percentages[lang] == max_percentage]
            # Check if at least one of them corresponds to the file extension
            for lang in languages:
                if extension in LANGS[lang]["extensions"]:
                    languages = [lang]
                    break

        # Print the result
        print("Analyzed file:", filepath)

        print()  # Percentages
        for key in percentages:
            print(f"{key}: {round(percentages[key], 2)}%")
        print()

        if languages:
            if len(languages) > 1:
                print(f"Detected languages: {', '.join(languages)}; None of them corresponds to the extension.")
            else:
                if extension in LANGS[languages[0]]["extensions"]:
                    print(f"Detected language: {languages[0]}; Language corresponds to the extension.")
                else:
                    print(f"Detected language: {languages[0]}; Language does not correspond to the extension.")
            cocomo.cocomoStart(filepath)
        else:
            print("Unable to recognize programming language.")
            choice = input("Do you want to run cocomo anyway? [y/n]: ")
            if choice.lower() == "y":
                cocomo.cocomoStart(filepath)

        print("File analysis ended")
        print()
        user_continue = input("Do you want to analyze another file? [y/n]: ").lower() == "y"


if __name__ == '__main__':
    main()
