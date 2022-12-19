#!python3

def calcola_COCOMO_BASE(filePath):
    M = 0
    Td = 0
    LOC = 0
    difficolta = ""

    valori_difficolta = {
        "facile": [2.4, 1.05, 2.5, 0.38],
        "intermedia": [3, 1.12, 2.5, 0.35],
        "difficile": [3.6, 1.12, 2.5, 0.32]
    }

    with open(filePath, 'r') as f:
        LOC = len(f.readlines())

    a = 0
    b = 0
    c = 0
    d = 0
    difficolta = ""
    if (LOC < 3000):
        difficolta = "facile"
    elif (LOC >= 3000 and LOC < 10000):
        difficolta = "intermedia"
    else:
        difficolta = "difficile"

    a = valori_difficolta[difficolta][0]
    b = valori_difficolta[difficolta][1]
    c = valori_difficolta[difficolta][2]
    d = valori_difficolta[difficolta][3]

    M = a * ((LOC / 1000)**b)
    Td = c * (M ** d)
    M = round(M, 2)
    Td = round(Td, 2)

    return f"LOC: {LOC}\nDifficolta': {difficolta}\nMesi uomo(ore): {M}\nTempo sviluppo(mesi): {Td}\n"
