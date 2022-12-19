"""
Descrizione: Programma in python che determina il linguaggio in cui è scritto un file di codice e controlla se
             corrisponde all'estensione.
"""

import os
import re
from collections import Counter
from keywords import LANGS

# Globali
PRODUCTION = True
DEBUG = False


# Funzioni
def conteggio_keywords(filepath):
    """
    Analizza un file di codice e ritorna un dizionario di percentuali pro i seguenti linguaggi:
    python, java, c, c++, c#, php, javascript, assembly 8086, batch, bash, powershell.

        Parameters:
            filepath (str): Percorso del file da analizzare

        Returns
            percentages (dict): Dizionario di percentuali per ogni linguaggio
    """
    # Apertura e lettura del file
    file = open(filepath, 'r')
    content = file.read()
    file.close()

    # Conteggio delle key words
    keywords = re.split("\n| |[(]|[{]|=|[+]|-|[*]|/|,|;|[.]|:|<|[$]", content)

    keyword_occurrences = Counter(keywords)  # Raggruppa le keyword
    keyword_occurrences.pop("")  # Elimina gli spazi vuoti
    unrecognized_keywords = dict.fromkeys(keyword_occurrences, 0)

    # Conta le keyword per ogni linguaggio
    counters = dict.fromkeys(LANGS, 0)
    for lang in LANGS:
        for key in keyword_occurrences:
            if key in LANGS[lang]["keywords"]:
                counters[lang] += keyword_occurrences[key]
                unrecognized_keywords[key] += 1

    # Conta le keyword non riconosciute
    counters["unrecognized"] = 0
    for key in unrecognized_keywords:
        if not unrecognized_keywords[key]:
            counters["unrecognized"] += keyword_occurrences[key]

    # Calcola le percentuali
    tot = sum(keyword_occurrences.values())
    percentages = {lang: (100 * counters[lang] / tot) for lang in counters}

    return percentages


def is_valid(filepath, verbose=False):
    """
    Controlla se un percorso esiste e se è un file.

        Parameters:
            filepath (str): Percorso del file
            verbose (bool): Se impostato a True visualizza i messaggi di errore

        Returns:
            validity (bool): Validità del file
    """
    if not os.path.exists(filepath):
        if verbose:
            print("File non esistente.")
        return False
    elif not os.path.isfile(filepath):
        if verbose:
            print("Il percorso immesso non è un file.")
        return False
    else:
        return True


def main():
    # Input file
    if DEBUG:
        filepath = "test/test.py"
    else:
        filepath = input('Inserisci il percorso del file: ')
        while not is_valid(filepath):
            filepath = input('Errore! Reinserisci il percorso del file: ')

    # Analizza il file
    percentages = conteggio_keywords(filepath)

    # Individua linguaggio ed estensione
    estensione = os.path.splitext(filepath)[1]

    lang_percentages = {key: percentages[key] for key in percentages if key != "unrecognized"}  # Escludi unrecognized
    max_percentage = max(lang_percentages.values())  # Individua la percentuale massima

    languages = None
    if max_percentage > 0:  # Se c'è almeno un linguaggio con percentuale maggiore di zero
        # Linguaggi con la percentuale massima
        languages = [lang for lang in lang_percentages if lang_percentages[lang] == max_percentage]
        # Cerca se almeno uno di essi corrisponde all'estensione del file
        for lang in languages:
            if estensione in LANGS[lang]["estensioni"]:
                languages = [lang]
                break

    # Stampa del risultato
    print("File analizzato:", filepath)

    print()  # Percentuali
    for key in percentages:
        print(f"{key}: {round(percentages[key], 2)}%")
    print()

    if languages:
        if len(languages) > 1:
            print(f"Linguaggi rilevati: {', '.join(languages)}; Nessuno di essi corrisponde all'estensione.")
        else:
            if estensione in LANGS[languages[0]]["estensioni"]:
                print(f"Linguaggio rilevato: {languages[0]}; Il linguaggio corrisponde all'estensione.")
            else:
                print(f"Linguaggio rilevato: {languages[0]}; Il linguaggio non corrisponde all'estensione.")
    else:
        print("Linguaggio di programmazione non riconosciuto.")


if __name__ == '__main__':
    main()
