# Import os per controllare l'esitenza del file scelto dall'utente
from os.path import exists

# Importo il dizionario 'LANGS' che contiene le le kewords dei linguaggi di programmazione scelti, le loro estensioni e un contatore
from keywords import LANGS


def conteggio_keywords(nome_file):
    # Aprertura e lettura del file
    file = open(nome_file, 'r')
    contenuto = file.read()

    # Conteggio delle key words
    for key, dict_interno in LANGS.items():
        for value in dict_interno['keywords']:
            dict_interno['contatore'] += contenuto.count(value)

    # Chiusura del file
    file.close()


def main():
    # nome_file = 'esempio.py'
    nome_file = input('Inserisci il percorso del file: ')
    while (exists(nome_file) == False):
        nome_file = input('Errore! Reinserisci il percorso del file: ')
    print('File trovato')

    conteggio_keywords(nome_file)

    linguaggio = None
    numero_keywords = []
    # Metto in un array i contatori
    for key, dict_interno in LANGS.items():
        numero_keywords.append(dict_interno['contatore'])

    print(numero_keywords)

    # Prendo il numero di keyword più grande
    nMAX = max(numero_keywords)

    # Assegno il linguaggio utilizzato
    key_list = list(LANGS.keys())
    for i in range(len(numero_keywords)):
        if numero_keywords[i] == nMAX:
            print(numero_keywords[i])
            linguaggio = key_list[i]
            break

    # Cerco l'estensione tra quelle presenti
    estensione = None
    for key, value in LANGS.items():
        if linguaggio == key:
            estensione = value['estensioni'][0]
            break

    # Stampa del risultato
    if nome_file.split('.')[len(nome_file.split('.')) - 1] == estensione:
        if linguaggio:
            print(
                f"Questo file è scritto in {linguaggio}, l'estensione combacia con il linguaggio di programmazione.")
    else:
        if linguaggio:
            print(
                f"Questo file è scritto in {linguaggio}, l'estensione non combacia con il linguaggio di programmazione.")
        else:
            print("Linguaggio di programmazione non trovato")


if __name__ == '__main__':
    main()
