"""
Description: Python program that determines the language in which a code file is written and checks
             if it matches its extension.
"""

import os
from extensions import *
from guesslang import Guess
import lizard

# Globals
PRODUCTION = True
DEBUG = False
LOG = True
LOG_FILE = "Result.txt"
cin = input
cout = print


# Functions
def count_keywords(source_code):
    """
    Analyzes a code and returns a dictionary of percentages of language compatibility

        Parameters:
            source_code (str): Code to analyze

        Returns
            percentages (dict): Dictionary of percentages for every language
    """
    guess = Guess()
    percentages = dict(guess.probabilities(source_code))
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
            cout("File does not exist.")
        return False
    elif not os.path.isfile(filepath):
        if verbose:
            cin("The path entered is not a file.")
        return False
    else:
        return True


def get_file_content(filepath):
    """
    Reads a file and returns its content

        Parameters:
            filepath (str): Path to the file

        Returns:
            content (str): Content of the file
    """
    f = open(filepath)
    content = f.read()
    return content


def main():
    global cin, cout
    # Output to file or terminal
    if LOG:
        __output_file__ = open(LOG_FILE, "w")

        def custom_output(string="", end="\n"):
            __output_file__.write(str(string) + end)
        cout = custom_output

    # Automatized input
    if DEBUG:
        __input_file__ = open("test/inputs.txt")

        def custom_input(string):
            cout(string, end="")
            line = __input_file__.readline()[:-1]
            cout(line)
            return line
        cin = custom_input

    user_continue = True
    while user_continue:
        # Input file
        filepath = cin('Insert file path: ')
        while not is_valid(filepath):
            filepath = cin('Error! Reinsert file path: ')

        # Analyze file and detect language
        percentages = count_keywords(get_file_content(filepath))
        cout(percentages)
        detected = max(percentages, key=percentages.get)
        cout(f"Detected language: {detected}")

        # Check the extension and rename if necessary
        extension = os.path.splitext(filepath)[1]
        cout(f"File extension: '{extension}'")
        if LANG_EXTENSIONS[detected] != extension:
            cout(f"Extension does not match detected language. Renaming...")
            os.rename(filepath, os.path.splitext(filepath)[0] + LANG_EXTENSIONS[detected])
            filepath = os.path.splitext(filepath)[0] + LANG_EXTENSIONS[detected]

        # Run code metrics, if possible
        if detected in LIZARD_SUPPORTED_LANGUAGES:
            cout(f"Running code metrics on '{filepath}'")
            code_metrics = lizard.analyze_file(filepath).__dict__
            for key, value in code_metrics["function_list"][0].__dict__.items():
                cout(f"{key}: {value}")

        # Ask user whether to analyze another file
        cout()
        user_continue = cin("Do you want to analyze another file? [y/n]: ").lower() == "y"


if __name__ == '__main__':
    main()
