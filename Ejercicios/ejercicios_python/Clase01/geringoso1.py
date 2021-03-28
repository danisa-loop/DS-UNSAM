# geringoso.py

cadena = 'Geringoso'
capadepenapa = ''
i = 0                  # índice para recorrer el ciclo for
for c in cadena:
    capadepenapa = capadepenapa + cadena[i]
    if (("a" in cadena[i]) == True):
        capadepenapa = capadepenapa + "pa"
    elif (("e" in cadena[i]) == True):
        capadepenapa = capadepenapa + "pe"
    elif (("i" in cadena[i]) == True):
        capadepenapa = capadepenapa + "pi"
    elif (("o" in cadena[i]) == True):
        capadepenapa = capadepenapa + "po"
    elif (("u" in cadena[i]) == True):
        capadepenapa = capadepenapa + "pu"
    else:
        capadepenapa
    i = i + 1
print(capadepenapa)