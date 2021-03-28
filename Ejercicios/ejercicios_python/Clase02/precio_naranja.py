# -*- coding: utf-8 -*-
#Ej 2.3
with open("../Data/precios.csv", "rt") as f:
    for line in f:
        row = line.split(",") #separo los elementos de las cadenas línea a línea
        if "Naranja" in row[0]: #busco naranja como ítem
            print("El precio de la naranja es:", float(row[1])) #imprimo el precio de la naranja como float