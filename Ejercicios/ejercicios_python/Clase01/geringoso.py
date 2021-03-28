cadena = 'geringosaurio'
print("La palabra a convertir en geringoso es: ", cadena)

capadepenapa = ''
vocales = "aeiou"

for c in cadena:
    if c in vocales:
        capadepenapa = capadepenapa + c + "p" + c
    else:
        capadepenapa = capadepenapa + c
print(cadena, "en geringoso es: ", capadepenapa)




 
