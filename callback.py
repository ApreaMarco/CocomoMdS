#!python3

import os
import re

# import dei programmi nella cartella scripts/
## import scripts.COCOMO_base as COCOMO_BASE

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

def read_keywords_from_file(filename):
    keywords = []
    with open("file_keywords/" + filename, "r") as f:
        for line in f:
            keywords.append(line.strip())
    return keywords

python_keywords = read_keywords_from_file("python_keywords.txt")
c_keywords = read_keywords_from_file("c_keywords.txt")
cp_keywords = read_keywords_from_file("c++_keywords.txt")
csharp_keywords = read_keywords_from_file("c#_keywords.txt")
java_keywords = read_keywords_from_file("java_keywords.txt")
javascript_keywords = read_keywords_from_file("javascript_keywords.txt")
php_keywords = read_keywords_from_file("php_keywords.txt")
assembly8086_keywords = read_keywords_from_file("assembly8086_keywords.txt")
powershell_keywords = read_keywords_from_file("powershell_keywords.txt")
batch_keywords = read_keywords_from_file("batch_keywords.txt")
bash_keywords = read_keywords_from_file("bash_keywords.txt")


def inizializzazioneDiz():
    dict = {".py": python_keywords,
            ".c": c_keywords,
            ".c++": cp_keywords,
            ".c#": csharp_keywords,
            ".java": java_keywords,
            ".js": javascript_keywords,
            ".php": php_keywords,
            ".asm": assembly8086_keywords,
            ".ps1": powershell_keywords,
            ".bat": batch_keywords,
            ".sh": bash_keywords
            }
    return dict


def conta_keyword(string, app):
    contatore = dict.fromkeys(list(app.keys()), 0)

    splitted = re.split("\n| |[(]|[{]|=|[+]|-|[*]|/|;", string)
    # rimuovere stringhe vuote
    splitted = [x for x in splitted if x]
    num_words = len(splitted)  # numero totale di parole nel file

    print("--Verifica del linguaggio del file")
    for ling, keywords in app.items():
        for keyword in keywords:
            contatore[ling] += splitted.count(keyword)

    # calcola la percentuale di parole chiave per ogni linguaggio
    print("--Percentuale keywords trovate per linguaggio")
    for ling, num_keywords in contatore.items():
        contatore[ling] = num_keywords / num_words * 100
        print(f"{ling}: {contatore[ling]:.2f}%")
        
    return contatore


def ricerca_tipo_file(app):
    ext = os.path.splitext(MY_PATH)[1]

    f = open(MY_PATH)

    contatore_keyword = conta_keyword(f.read(), app)
    print("--Contatore_keyword:\n", contatore_keyword)

    # trova il linguaggio con il più alto numero di parole chiave
    linguaggio = max(contatore_keyword, key=contatore_keyword.get)
    # trova il numero di parole chiave per il linguaggio trovato
    num_keywords = contatore_keyword[linguaggio]

    # confronta il numero di parole chiave trovate per il linguaggio trovato
    # con il numero di parole chiave trovate per gli altri linguaggi
    for ling, keywords in contatore_keyword.items():
        if ling != linguaggio and num_keywords == keywords:
            linguaggio = "neutro"

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

##    print(COCOMO_BASE.calcola_COCOMO_BASE(MY_PATH))

    print(f"--Estensione file: {estensioneFile}")
    print(f"--Linguaggio elaborato: {linguaggioElaborato}")
    print("\n--IL LINGUAGGIO E' UGUALE ALL'ESTENSIONE" if isEstensioneCorretta else "\n--IL LINGUAGGIO NON E' UGUALE ALL'ESTENSIONE")


if __name__ == "__main__":
    main()
