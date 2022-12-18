def funzione1() :
    print ("Sono la funzione 1")


def funzione2() :
    print ("Sono la funzione 2")


def funzione3() :
    print ("Sono la funzione 3")


def funzione4() :
    print ("Sono la funzione 4")


def inizializzazioneDiz() :
    dict = {"key1": funzione1,
            "key2": funzione2,
            "key3": funzione3,
            "key4": funzione4,
        }
    return dict


def lanciatore(dict) :
    listaKey = dict.keys()
    scelta = 'Null'
    while scelta not in listaKey:

        print("--- Dominio scelte ---")
        i = 1

        for key in listaKey:
            print(f'{i}: {key}')
            i += 1

        scelta = input ("Scegli fra:")
    print(f'chiave: {scelta}-> valore: {dict[scelta]}')
    return dict[scelta]

def extCheck(filename):
    return filename.endswith(".py")

def main() :
    app = inizializzazioneDiz()
    funzione = lanciatore(app)
    funzione()


if __name__ == "__main__":
    main()