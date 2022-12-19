import re
from os.path import exists

def metricheSoftwere():
    #Inizializzo le variabili
    righeCommentate = 0
    eseguibili = 0
    funzioni = 0
    i = 0
    f = 0
    w = 0

    for line in contenuto:
        if re.search("#", line):
            righeCommentate += 1       #Conto le righe commentate del programma
        else:
            eseguibili += 1            #Conto le righe eseguibili del programma
        if re.search("def", line):
            funzioni += 1              #Conto funzioni del programma
        if re.search("if", line):
            i += 1                     #Conto il numero di 'if' del programma
        if re.search("for", line):
            f += 1                     #Conto il numero di cicli 'for' del programma
        if re.search("while", line):
            w += 1                     #Conto il numero di cicli 'while' del programma
    
    #Scrivo il file di uscita
    scrittura = "Righe di codice totali = " + str(LOC) + "\n" + "Righe eseguibili = " + str(eseguibili) + "\n" + "Righe commentate = " + str(righeCommentate) + "\n" + "Numero di funzioni = " + str(funzioni) + "\n" + 'Numero di istruzioni "if" = ' + str(i) + "\n" + 'Numero di istruzioni "for" = ' + str(f) + "\n" + 'Numero di istruzioni "while" = ' + str(w) + "\n\n"
    outputFile.write("Metriche del softwere:" + "\n" + scrittura)


def complessitaCiclomatica():
    #Inzializzo la variabile
    complessita = 0
    for line in contenuto:
        if (re.search("if", line) or re.search ("else", line) or re.search ("elif", line) or re.search ("for", line) or re.search ("while", line)):
            complessita += 1 #Conto il numero di 'if', 'else', 'elif', 'for', 'while'

    #Scrivo il file di uscita
    scrittura = "Complessità ciclomatica del del programma = " + str(complessita) + "\n\n"
    outputFile.write(scrittura)


def CocomoBase(dif):
    #Inizializzo le variabili
    sempliceLOC = [2.4, 1.05, 2.5, 0.38]
    intermediaLOC = [3, 1.12, 2.5, 0.35]
    complessaLOC = [3.6, 1.12, 2.5, 0.32]

    #Assegno il valore alle variabili
    if (dif == 1):
        difficolta = "Facile" #Assegno la difficlota
        a = sempliceLOC[0] # Numero di righe in migliaia di righe
        b = sempliceLOC[1] # Economie di scala
        c = sempliceLOC[2] # Valore che tiene conto della difficolta del programma
        d = sempliceLOC[3] # Valore che tiene conto della difficolta del programma
    elif (dif == 2):
        difficolta = "Intermedia"
        a = intermediaLOC[0]
        b = intermediaLOC[1]
        c = intermediaLOC[2]
        d = intermediaLOC[3]
    else:
        difficolta = "Complessa"
        a = complessaLOC[0]
        b = complessaLOC[1]
        c = complessaLOC[2]
        d = complessaLOC[3]

    #Calcolo i mesi uomo e il tempo di sviluppo
    mesiUomo = a * ((LOC / 1000)**b)
    tempoSviluppo = c * (mesiUomo ** d)

    #Scrivo il file in uscita
    scrittura(difficolta, tempoSviluppo, mesiUomo)

def CocomoIntermedio(dif):
    #Inizializzo le variabili
    sempliceLOC = [3.2, 1.05, 2.5, 0.38]
    intermediaLOC = [3, 1.12, 2.5, 0.35]
    complessaLOC = [2.8, 1.2, 2.5, 0.32]

    #Assegno la difficoltà
    if (dif == 1):
        difficolta = "Facile" #Assegno la difficlota
        a = sempliceLOC[0] # Numero di righe in migliaia di righe
        b = sempliceLOC[1] # Economie di scala
        c = sempliceLOC[2] # Valore che tiene conto della difficolta del programma
        d = sempliceLOC[3] # Valore che tiene conto della difficolta del programma
    elif (dif == 2):
        difficolta = "Intermedia"
        a = intermediaLOC[0]
        b = intermediaLOC[1]
        c = intermediaLOC[2]
        d = intermediaLOC[3]
    else:
        difficolta = "Complessa"
        a = complessaLOC[0]
        b = complessaLOC[1]
        c = complessaLOC[2]
        d = complessaLOC[3]

    #Inizializzo i valori del costDriver
    costDriver1 = {"ACAP": 1.46,
                "AEXP" : 1.29,
                "CPLX" : 0.7, 
                "DATA" : 0, 
                "LEXP" : 1.14,
                "MCDP" : 1.24, 
                "PCAP" : 0.75, 
                "RELY" : 1.23, 
                "SCED" : 1.23, 
                "STOR" : 0, 
                "TIME" : 0, 
                "TOOL" : 1.24, 
                "TURN" : 0, 
                "VEXP" : 1.21, 
                "VIRT" : 0}

    costDriver2 = {"ACAP": 1.19,
                "AEXP" : 1.13,
                "CPLX" : 0.85, 
                "DATA" : 0.94, 
                "LEXP" : 1.07,
                "MCDP" : 1.1, 
                "PCAP" : 1.17, 
                "RELY" : 0.88, 
                "SCED" : 1.08, 
                "STOR" : 0, 
                "TIME" : 0, 
                "TOOL" : 1.1, 
                "TURN" : 0.87, 
                "VEXP" : 1.10, 
                "VIRT" : 0.87}

    costDriver3 = {"ACAP": 1,
                "AEXP" : 1,
                "CPLX" : 1, 
                "DATA" : 1, 
                "LEXP" : 1,
                "MCDP" : 1, 
                "PCAP" : 1, 
                "RELY" : 1, 
                "SCED" : 1, 
                "STOR" : 1, 
                "TIME" : 1, 
                "TOOL" : 1, 
                "TURN" : 1, 
                "VEXP" : 1, 
                "VIRT" : 1}

    costDriver4 = {"ACAP": 0.86,
                "AEXP" : 0.91,
                "CPLX" : 1.15, 
                "DATA" : 1.08, 
                "LEXP" : 0.95,
                "MCDP" : 0.91, 
                "PCAP" : 0.86, 
                "RELY" : 1.15, 
                "SCED" : 1.04, 
                "STOR" : 1.06, 
                "TIME" : 1.11, 
                "TOOL" : 0.91, 
                "TURN" : 1.07, 
                "VEXP" : 0.9, 
                "VIRT" : 1.15}

    costDriver5 = {"ACAP": 0.71,
                "AEXP" : 0.86,
                "CPLX" : 1.3, 
                "DATA" : 1.16, 
                "LEXP" : 0,
                "MCDP" : 0.82, 
                "PCAP" : 0.7, 
                "RELY" : 1.4, 
                "SCED" : 1.1, 
                "STOR" : 1.21, 
                "TIME" : 1.3, 
                "TOOL" : 0.83, 
                "TURN" : 1.15, 
                "VEXP" : 0, 
                "VIRT" : 1.3}

    costDriver6 = {"ACAP": 0,
                "AEXP" : 0,
                "CPLX" : 1.65, 
                "DATA" : 0, 
                "LEXP" : 0,
                "MCDP" : 0, 
                "PCAP" : 0, 
                "RELY" : 0, 
                "SCED" : 0, 
                "STOR" : 1.56, 
                "TIME" : 1.66, 
                "TOOL" : 0, 
                "TURN" : 0, 
                "VEXP" : 0, 
                "VIRT" : 0}

    #Faccio scegliere il cost driver
    print("\nScegli fra i seguenti Cost Driver:\n"
        "ACAP" + "\n"
        "AEXP" + "\n"
        "CPLX" + "\n"
        "DATA" + "\n"
        "LEXP" + "\n"
        "MCDP" + "\n"
        "PCAP" + "\n"
        "RELY" + "\n"
        "SCED" + "\n"
        "STOR" + "\n"
        "TIME" + "\n"
        "TOOL" + "\n"
        "TURN" + "\n"
        "VEXP" + "\n"
        "VIRT" + "\n"
        )
    scelta = input("Inserire il nome del Cost Driver: ")
    while (scelta not in costDriver1):
        scelta = input("\nErrore! Nome non valido. Reinserire Cost Driver: ")

    #Chiedo la difficoltà 
    dif = 0
    print("\nScegli fra i seguenti valori:\n\n"
        "Very low = 1" + "\n"
        "Low = 2" + "\n"
        "Nominal = 3" + "\n"
        "High = 4" + "\n"
        "Very high = 5" + "\n"
        "Extra high = 6" + "\n")
    dif = int(input("Inserisci una valore tra 1 e 6: "))
    while (dif < 1 or dif > 6):
        dif = int(input("\nErrore! Reinserisci un valore tra 1 a 6: "))

    #Assegno il costDriver
    if (dif == 1):
        costDriver = costDriver1
    elif (dif == 2):
        costDriver = costDriver2
    elif (dif == 3):
        costDriver = costDriver3
    elif (dif == 4):
        costDriver = costDriver4
    elif (dif == 5):
        costDriver = costDriver5
    elif (dif == 6):
        costDriver = costDriver6

    #Calcolo i mesi uomo e il tempo di sviluppo
    if (costDriver[scelta] == 0):
        mesiUomo = a * ((LOC / 1000) ** b)
    else:
        mesiUomo = a * ((LOC / 1000) ** b) * (costDriver[scelta] * 15)
    
    tempoSviluppo = c * (mesiUomo ** d)

    #Scrivo il file in uscita
    scrittura(difficolta, tempoSviluppo, mesiUomo)

def scrittura(difficolta, tempoSviluppo, mesiUomo):
    #Scrivo il file di uscita
    if mod == 2:
        cocomo = "base"
    else:
        cocomo = "intermedio"
    scrittura = "Numero di righe di codice = " + str(LOC) + "\n" + "Difficolta = " + str(difficolta) + "\n" + "Mesi uomo = " + str(round(mesiUomo, 2)) + "\n" + "Tempo di sviluppo = " + str(round(tempoSviluppo, 2)) + "\n\n"
    outputFile.write("Cocomo " + cocomo + ":" + "\n" + scrittura)

def cocomoStart(filepath):
    #Prendo il filepath del file
    global contenuto
    while (exists(filepath) == False and filepath.lower().endswith(".py") == False):
        filepath = input("Errore! Reinserisci il filepath del file Python: ")
    print("File trovato")
    file = open(filepath, 'r')
    contenuto = file.readlines()
    
    #Scelta della modalità
    print("\nScegli fra le seguenti modalità: "+ "\n\n"
        "Metriche del softwere = 1" + "\n"
        "Complessita ciclomatica = 2" + "\n"
        "Cocomo base = 3" + "\n"
        "Cocomo intermedio = 4" + "\n"
        "Tutte le operazioni = 5" + "\n")
    
    global mod
    mod = int(input("Inserisci la modalità tra 1 e 5: "))
    while (mod < 1 or mod > 5):
        mod = int(input("\nErrore! Reinserisci un valore tra 1 a 5: "))
    
    #Apro il file in scrittura
    global outputFile
    outputFile = open("Risultato.txt", "w")
    outputFile.write("Caratteristiche del file '" + filepath +"'\n\n")

    #Conteggio del numero di righe del file
    global LOC
    LOC = 0
    for line in contenuto:
        LOC += 1

    #In base alla modalità scelta chiamo la funzione inerente
    if mod == 1:
        metricheSoftwere()
    elif mod == 2:
        complessitaCiclomatica()
    else:
        #Chiedo la difficoltà del file
        print("\nScegli fra le le seguenti difficoltà\n\n1 = Semplice\n2 = Intermedia \n3 = Complessa\n")
        dif = int(input("Inserire la difficoltà del programma tra 1 e 3: "))

        while(dif < 1 or dif > 3):
            dif = int(input("\nErrore! Reinserire la difficoltà del programma tra 1 e 3: "))
        
        if mod == 3:
            CocomoBase(dif)
        elif mod == 4:
            CocomoIntermedio(dif) 
        else:
            #Se la modalità è 5 allora chiama tutte le funzioni
            metricheSoftwere()
            complessitaCiclomatica()
            CocomoBase(dif)
            CocomoIntermedio(dif)

    print("\nScrittura completata")
    file.close() #Chiudo il file in lettura
    outputFile.close() #Chiudo il file in scrittura