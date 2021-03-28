# -*- coding: utf-8 -*-
#Ejercicio 2.7
def buscar_precio(fruta):
    f = open("../Data/precios.csv", "rt")
    data = f.read()
    if fruta not in data: #primero me fijo que fruta no figure en todo el archivo antes de iterar línea a línea (sino me escribe que no se encuentra en el listado tantas veces como líneas en el archivo)
        print(fruta, "no figura en el listado de precios.")
        f.close()
    else:
        f = open("../Data/precios.csv", "rt")
        for line in f: #abro nuevamente el archivo, pero de a líneas para ingresar en c/u
            row = line.split(",") #separo los elementos de las cadenas línea a línea
            if fruta in row[0]: #busco fruta como ítem
                print("El precio de un cajón de", fruta, "es:", float(row[1])) #imprimo el precio de un cajón de fruta
        f.close()
        
print(buscar_precio("Naranja"))
#Funciona pero copia un None raro al final.
#%%
precios = {}

with open("../Data/precios.csv", "rt") as f:
    for line in f:
        row = line.split(",")
        precios[row[0]] = float(row[1])
#No anda