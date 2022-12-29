#!python3

import os

CONF_FILES = [
    "config/python_keywords.conf",
    "config/c_keywords.conf",
    "config/c++_keywords.conf",
    "config/c#_keywords.conf",
    "config/java_keywords.conf",
    "config/javascript_keywords.conf",
    "config/php_keywords.conf",
    "config/assembly_keywords.conf",
    "config/powershell_keywords.conf",
    "config/batch_keywords.conf",
    "config/bash_keywords.conf",
]

isException = False
exceptionMessage = "\n"


def write_exception(msg):
    global isException, exceptionMessage
    if not isException:
        isException = True
    exceptionMessage += f"\t{msg}\n"


def check_files():
    # take dir name of this script
    current_dir = __file__.split("\\")[-2]
    # take abs path of the project
    DIR_PATH = os.path.dirname(__file__).replace(current_dir, '')
    print(f"---Project dir: {DIR_PATH}")

    FILES = [
        "scripts",
        "scripts/base_COCOMO.py",
        "config"
    ]
    FILES += CONF_FILES

    print("---Check files existance")
    for _file in FILES:
        if not os.path.exists(DIR_PATH+_file):
            file_ext = os.path.splitext(_file)[1]
            if (file_ext == ''):
                os.mkdir(DIR_PATH + _file)
                print(f"---Directory {_file} created")
            elif (file_ext == ".conf"):
                # create .conf file
                open(DIR_PATH+_file, 'w')
                print(f"---File {_file} created")
            else:
                write_exception(f"\tFILE {_file} is inexistent")
        elif (os.path.splitext(_file)[1] == ".conf"):
            # check if .conf file is empty and it has the correct syntax
            with open(DIR_PATH+_file, 'r') as conf_file:
                lines = conf_file.readlines()
                if (not lines):
                    # empty file
                    write_exception(f"\tFILE {_file} is empty")
                    continue

                if (not lines[0].startswith("LANG=")):
                    write_exception(f"\tFILE {_file} hasn't LANG component")
                if (not lines[1].startswith("KEYWORDS=")):
                    write_exception(
                        f"\tFILE {_file} hasn't KEYWORDS component")

    if (isException):
        raise Exception(exceptionMessage)

    print("---All files have been checked succesfully\n")


def main():
    check_files()


if __name__ == "__main__":
    main()
