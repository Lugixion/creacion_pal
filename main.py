from os import system
from time import sleep, time
from random import randint
import unidecode
from pals import words

"""
def scoreboard(points):
    score = db["scoreboard"]
    print("RECORDS\n--------------\n\n")
    
    for val in range(1,10):
        print(str(val) + "- " + score[val][0] + " : " + str(score[val][1]) + " puntos")
"""

def endgame(numb, words, configs):
    system("clear")
    print("Número de palabras encontradas: " + str(numb))
    sleep(1)
    print("Palabras encontradas:")

    for word in words:
        sleep(.4)
        print("- " + word)

    points = round((numb / configs[1]) * 100)
    
    print("\nPuntuación total: " + str(points) + " puntos.") 

    input("\nPresiona Enter para continuar.\n")
    system("clear")
    sleep(2)

    # scoreboard(points)

    return

def splitw(word, accent):
    ret = []

    if accent == "n":
        for let in word:
            ret.append(unidecode.unidecode(let))
    else:
        for let in word:
            ret.append(let)

    return ret

def play(configs):

    global leng
    leng = []
    avwords = []
    avwordsu = []

    system("clear")
    print("Inicializando...", end="\r")

    print(configs)

    for i in words:
        if len(i) >= configs[2]:
            avwordsu.append(i)

    for i in words:
        if len(i) >= configs[0]:
            avwords.append(i)

    rword = avwords[randint(0,len(avwords))]

    cont = 0

    selwords = []

    if configs[3] == 'n':
        temp = []
        for i in avwordsu:
            temp.append(unidecode.unidecode(i))
        
        avwordsu = []

        for i in temp:
            avwordsu.append(i)

        del temp

    wlets = splitw(rword, configs[3])

    for letter in rword:
        if configs[3] == "n":
            wlets.append(letter)

    print("Inicialización finalizada.")
    sleep(3)
    system("clear")

    sttime = time()
    print("PALABRA: " + rword.upper() + "\n\n")

    while True:

        if configs[3] == "n":
            pal = unidecode.unidecode(input("Introduzca una palabra: ").lower())
        else:
            pal = input("Introduzca una palabra: ").lower()

        if pal in avwordsu and pal not in selwords:
            try:
                for let in pal:
                    wlets.remove(let)

                cont += 1
                print("¡Correcto!\n")
                selwords.append(pal)    
            except ValueError:
                print("¡Te faltan letras!\n")
        else:
            print("¡Esa palabra no es válida!\n")

        entime = time()

        if (entime - sttime) >= (configs[1] * 60):
            print("\n\n¡El juego ha finalizado!")
            sleep(3)
            endgame(cont, selwords, configs)
            break

        wlets = splitw(rword, configs[3])

    main(True, configs)


def configame(strs, conf, cfr):
    system("clear")
    
    if cfr:
        r = input("¿Desea volver a jugar con las mismas configuraciones de la partida anterior? (s/n)\n> ").lower()
        if r in ["s", "si", "sí"]:
            print("Repitiendo juego...")
            sleep(2)
            play(conf)
        elif r in ["n", "no"]:
            configame(strs, None, False)
        else:
            print("Selección desconocida.")
            sleep(2)
            configame(strs, None, False)
    else:
        configs = []

        print("CONFIGURACIÓN DEL JUEGO\n--------------------------")
        print("Configuración de la máquina.\n")

        try:
            lenwords = int(input("Mínimo de letras en las palabras: "))
            lentime = int(input("Tiempo de juego (en minutos): "))

            configs.append(lenwords)
            configs.append(lentime)
        except ValueError:
            print("Tiene que ser un número.")
            sleep(3)
            configame(strs, None, False)

        system("clear")

        print("CONFIGURACIÓN DEL JUEGO\n--------------------------")
        print("Configuración del usuario.\n")

        print("Mín letras (máquina): " + str(lenwords))
        print("Tiempo: " + str(lentime) + "\n")

        try:
            lenus = int(input("Mínimo de letras en las palabras que el usuario elija: "))
            configs.append(lenus)
        except ValueError:
            print("Tiene que ser un número.")
            sleep(3)
            configame(strs, None, False)

        tild = input("¿Las tildes influyen? (s,n): ").lower()

        if tild in ["s", "si", "sí"]:
            configs.append("s")
        elif tild in ["n", "no"]:
            configs.append("n")
        else:
            print("Selección inválida.")
            sleep(3)
            configame(strs, None, False)

        system("clear")
        print("¿Seguro deseas seguir con la siguiente configuración?:\n")

        print("Mínimo de letras (máquina): " + str(configs[0]))
        print("Tiempo de juego: " + str(configs[1]) + "\n")

        print("Mínimo de letras (usuario): " + str(configs[2]))    

        if configs[3] == "s":
            print("Tildes influyen: SÍ")
        else:
            print("Tildes influyen: NO")

        sure = input("(s,n) > ").lower()

        if sure in ["s", "si", "sí"]:
            play(configs)
        else:
            print("Operación cancelada.")
            sleep(3)
            system("clear")
            main(False, None)

def howorks():
    system("clear")
    print("Una palabra completamente aleatoria saldrá en la pantalla.\nUsando sus letras exactas, tienes que crear nuevas\npalabras válidas. Mientras en menos tiempo\nganes más palabras, conseguirás más puntos.")
    input("\nPresiona Enter para volver al menú.\n")
    system("clear")
    sleep(2)
    main(False, None)

def main(cfr, conf):
    print("CREACIÓN DE PALABRAS\n---------------")
    print("[1] Jugar\n[2] ¿Cómo funciona?\n")

    sel = input("> ").lower()

    if sel in ["1", "jugar"]:
        configame(words, conf, cfr)
    elif sel in ["2", "¿cómo funciona?", "¿como funciona?", "como funciona?", "cómo funciona?"]:
        howorks()
    else:
        print("Selección desconocida.")
    

main(False, None)          

"""
TO DO

- Scoreboard system (Secondary task)

- Make GUI
"""
