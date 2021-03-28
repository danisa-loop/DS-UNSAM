frase = 'todos somos programadores'
palabras = frase.split()
for palabra in palabras:
    if palabras[-2:] == "o":
        palabra.replace("e")
    frase_t = palabra
    print(frase_t)