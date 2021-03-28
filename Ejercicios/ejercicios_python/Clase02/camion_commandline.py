# -*- coding: utf-8 -*-
#Ej. 2.10:

import csv
import sys

def costo_camion(nombre_archivo):
    with open(nombre_archivo) as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        rows = csv.reader(f)
        headers = next(rows)
        costo = 0 #inicializo costo en 0 ya que quiero que se vaya sumando al iterar línea a línea
        for row in rows:
            try:    
                cantidad = int(row[1])
                precio = float(row[2]) 
                costo += cantidad*precio
            except ValueError:
                print("Warning!")    
        return costo

if len(sys.argv) == 2: #Agrego estos comandos para que se pueda llamar a la función junto con el archivo de data en la misma línea en la consola
    nombre_archivo = sys.argv[1]    
else:
    nombre_archivo = "../Data/camion.csv"

costo = costo_camion(nombre_archivo)
print("Costo total:", costo)
