#!python3

import os
import re

__author__ = ["Rajapaksha Kasun", "Serratore Federico", "Villardi Riccardo"]
__copyright__ = "Copyright 2022"
__version__ = "1.0.0"
__maintainer__ = ["Rajapaksha Kasun",
                  "Serratore Federico", "Villardi Riccardo"]
__email__ = ["19221@studenti.marconiverona.edu.it",
             "19169@studenti.marconiverona.edu.it", "19245@studenti.marconiverona.edu.it"]

# pulire terminale
os.system("cls")

MY_PATH = ""    # percorso in input


def inizializzazioneDiz():
    dict = {".py": [ "def", "if", "for", "in", "and", "not", "or", "print", "class", "try", "except", "import", "from", "as",
               "lambda" ],
            ".c": [ "return", "struct", "union", "int", "char", "float", "if", "else", "typedef", "const",
                "static", "enum", "void", "for", "while" ],
            ".c++": [ "if", "else", "for", "while", "return", "struct", "int", "char", "float", "double",  "class", "private",
                "public", "inline", "const", "static", "template", "namespace", "using",
                "new", "delete", "protected", "friend", "virtual" ],
            ".c#": [ "namespace", "Console.WriteLine", "Console.Write", "int", "double", "char", "string", "bool", "long",
                "if","else","else if","switch","break","foreach","continue","for","sort", "static", "void", "protected", "private",
                "public", "internal", "get", "set", "abstract", "AppendText", "Copy", "Create", "try", "catch" ],
            ".java": [ "finally", "return", "void", "class", "implements","public", "private", "protected", "if", "else", "for",
                "while", "do", "try", "catch",  "null", "this", "super", "new", "import", "package", "interface", "extends" ],
            ".js": ["if", "else", "finally", "return", "var", "let", "const", "this", "new", "delete", "typeof",
                "instanceof", "null", "undefined", "NaN", "function", "Infinity", "for", "while", "do", "try", "catch" ],  
            ".php": [ "?php", "echo", "?", "$", "print", "public", "function", "strlen", "str_word_count", "strrev", "rand",
                "define", "switch", "default", "while", "for", "foreach", "array", "$_SERVER", "$_POST", "$_GET", "preg_match",
                "post" ], 
            ".asm": [ "MOV", "BX", "CX", "SI", "DI", "BP", "AX", "INT", "VAR", "RET", "END", "PRINT", "ORG", "SUB", "DIV",
                "DB", "DW", "DUP", "LEA", "EQU", "CALL", "ADD", "CMP", "AND", "TEST", "OR", "XOR", "IMUL", "IDIV", "NOT", "NEG", "JMP" ], 
            ".ps1": [ "Get-Command", "-Name", "-Verb", "Select-Object", "Get-Process", "$",
                "function", "param", "begin", "end", "if", "else", "for", "foreach", "while", "return", "try", "catch", "clear",
                "Copy-Item", "Remove-Item", "Move-Item", "Test-Path", "Get-Content", "do" ],
            ".bat": [ "@echo", "ver", "cd", "Cls", "", "copy", "Rem", "from", "if", "del", "dir", "PATH", "exit", "set", "FIND", "CHKDSK",
                "OFF", "cmd" ,"comp", "@ECHO", "VER", "CD", "CLS", "COPY", "REM", "FROM", "IF", "DEL", "DIR", "PATH", "EXIT", "SET",
                "FIND", "CHKDSK", "OFF", "CMD", "COMP", "ECHO"],
            ".sh": [ "ls", "touch", "mkdir", "man", "pwd", "grep", "cd", "mv", "rmdir", "locate", "less", "compgen", "cat", "exit",
                "history", "cp", "kill", "sleep", "if", "for", "select" ]
            }
    return dict


def conta_keyword(string, app):
    contatore = dict.fromkeys(list(app.keys()), 0)

    splitted = re.split("\n| |[(]|[{]|=|[+]|-|[*]|/|;", string)
    # rimuovere stringhe vuote
    splitted = [x for x in splitted if x]

    print("--Verifica del linguaggio del file")
    for ling, keywords in app.items():
        for keyword in keywords:
            contatore[ling] += splitted.count(keyword)

    return contatore


def ricerca_tipo_file(app):
    ext = os.path.splitext(MY_PATH)[1]

    f = open(MY_PATH)

    contatore_keyword = conta_keyword(f.read(), app)
    print("--Contatore_keyword:\n", contatore_keyword)

    linguaggio = max(contatore_keyword, key=contatore_keyword.get)

    return linguaggio, ext


def richiestaInput():
    global MY_PATH

    # richiesta input del file
    while True:
        MY_PATH = input("---INSERIRE FILE DA LEGGERE:\n").strip()

        # controllare e rimuovere eventuali doppi apici a inizio e fine input
        if ((len(MY_PATH) > 0) and (MY_PATH[0] == '"' or MY_PATH[len(MY_PATH)-1] == '"')):
            MY_PATH = MY_PATH.replace('"', "")

        # esce dal ciclo quando percorso esiste ed e' un file
        if (os.path.exists(MY_PATH)):
            # controlla se percorso e' un file
            if (os.path.isfile(MY_PATH)):
                break

            print("---Percorso selezionato non e' un file\n")

        print("---File NON esistente\n")


def main():
    print("--ANALIZZATORE DI LINGUAGGI DI PROGRAMMAZIONE--")
    # INPUT
    richiestaInput()

    app = inizializzazioneDiz()

    linguaggioElaborato, estensioneFile = ricerca_tipo_file(app)

    isEstensioneCorretta = linguaggioElaborato == estensioneFile

    # OUTPUT
    print("\n--Elaborazione terminata con successo")
    print(f"--Estensione file: {estensioneFile}")
    print(f"--Linguaggio elaborato: {linguaggioElaborato}")
    print("\n--IL LINGUAGGIO E' UGUALE ALL'ESTENSIONE" if isEstensioneCorretta else "\n--IL LINGUAGGIO NON E' UGUALE ALL'ESTENSIONE")


if __name__ == "__main__":
    main()
