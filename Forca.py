from random import choice
center = 0


# ---------------------------------------------------------------------------


# ------------------NAO USE ACENTOS NAS LETRAS!


def ClearScreen():
    print()


def ChangeLetter():
    global letra, palavra, letrasEncontradas
    return_tmp = ""
    for p, l in enumerate(palavra):
        if (l == letra):
            return_tmp += l
        else:
            return_tmp += letrasEncontradas[p]
    return return_tmp


def ShowFoundLetters():
    global letrasEncontradas
    print((center - len(letrasEncontradas) + 5) * " ", end="")
    for l in letrasEncontradas:
        print(l + " ", end="")
    print()


def ShowLettersUsed():
    global letrasUsadas
    print((center - 2) * " " + "LETRAS USADAS: ")
    print((center - int(len(letrasUsadas) / 2) + 5) * " ", end="")
    for l in letrasUsadas[0:-2]:
        print(l, end="")
    print()


def DrawBody():
    global partesDoCorpo, center, error
    if (error == 1):
        partesDoCorpo[0] = "O"  # cabeca
    elif (error == 2):
        partesDoCorpo[1] = "|"  # tronco cima
    elif (error == 3):
        partesDoCorpo[2] = "|"  # tronco baixo
    elif (error == 4):
        partesDoCorpo[3] = "/"  # perna esquerda
    elif (error == 5):
        partesDoCorpo[4] = " \\"  # perna direita
    elif (error == 6):
        partesDoCorpo[5] = "/"  # braco esquerdo
    elif (error == 7):
        partesDoCorpo[6] = "\\"  # braco direito

    print(center * " " + "   ____ ")
    print(center * " " + "  /    |")
    print(center * " " + " /     " + partesDoCorpo[0])
    print(center * " " + "|     " + partesDoCorpo[5] + partesDoCorpo[1] + partesDoCorpo[6])
    print(center * " " + "|      " + partesDoCorpo[2])
    print(center * " " + "|     " + partesDoCorpo[3] + partesDoCorpo[4])
    print(center * " " + "| ")


def UpdateScreen():
    ClearScreen()
    print((center - 6) * " " + "<ESPAÇO IGUAL A HÍFEN>")
    ShowLettersUsed()
    DrawBody()
    ShowFoundLetters()


# --------------------------------------------------------------------------------------------

error = 0

aux = "abcdefghijklmnopqrstuvwxyz-"
partesDoCorpo = [" ", " ", " ", " ", " ", " ", " "]
letrasUsadas = ""

# palavra = "teste"

print((center - 4) * " " + "[1] Jogar sozinho\n" + (center - 4) * " " + "[2] Jogar com alguém")

tipo = int(input((center - 4) * " " + "Opção> "))

if (tipo == 1):

    # Voce pode adicionar mais palavras se quiser ----------------

    # Nomes de animais
    ani = ["raposa", "tubarao", "cobra", "jabuti", "baleia", "cachorro", \
           "gato", "peixe", "arraia", "alce", "pinguim", "rato", "avestruz", "macaco", \
           "boi", "vaca"]

    # Nomes de frutas
    fru = ["banana", "laranja", "uva", "morango", "manga", "melancia", "pera", \
           "jaca", "cereja", "goiaba", "acerola", "abacate", "cacau", "caqui", "carambola", \
           "groselha", "jabuticaba", "jambo", "kiwi", "amora", "abacaxi"]

    print((center - 4) * " " + "[1] Animais" + (center - 4) * " " + "[2] Frutas")

    tipo = int(input((center - 4) * " " + "Opção> "))

    if (tipo == 1):
        palavra = choice(ani)
    else:
        palavra = choice(fru)

else:
    palavra = input(center * " " + "Palavra> ").lower().replace(" ", "-")


letrasEncontradas = "_" * len(palavra)
UpdateScreen()


# codigo principal
while letrasEncontradas != palavra and error < 7:
    try:
        letra = input(center * " " + "Letra> ")[0].lower()
    except:
        letra = ""

    if(letra == " "):
        letra = "-"

    if (letra not in letrasUsadas and letra in aux):
        letrasUsadas += letra + ", "
        if (letra in palavra):
            letrasEncontradas = ChangeLetter()
        else:
            error += 1

    UpdateScreen()

ClearScreen()

if (error == 7):
    print(center * " " + "Você perdeu, APEDEUTA!")
else:
    print(center * " " + "Você ganhou, parabens Apedeuta!")
print((center - int(len("a palavra era " + palavra) / 2) + 5) * " " + "a palavra era", palavra)