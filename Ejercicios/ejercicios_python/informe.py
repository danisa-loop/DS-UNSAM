# -*- coding: utf-8 -*-
#Ej 2.15

import csv 

def leer_camion(nombre_archivo):
    #lee el contenido del archivo con los datos del camión y lo devuelve como tupla
    camion = [] 
    with open(nombre_archivo, "rt") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        rows = csv.reader(f) #acá defino las filas
        headers = next(rows) #encabezado
        for row in rows: #filas definidas
            try:    
                lote = (row[0], int(row[1]), float(row[2]))
                camion.append(lote)
            except ValueError:
                print("Warning!")    
        return camion

camion = leer_camion("../Data/camion.csv")
print("info tupla:", camion)

#%%
#Ejercicio 2.16
#Esta fc siempre me escribe la última fila, NO ANDA
def leer_camion(nombre_archivo):
    #lee el contenido del archivo con los datos del camión y lo devuelve como diccionario
    camion = {} 
    tipo = []
    with open(nombre_archivo, "rt") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        rows = csv.reader(f) #acá defino las filas
        headers = next(rows) #encabezado
        for row in rows: #filas definidas
            try:    
                camion["nombre"] = row[0] 
                camion["cajones"] = int(row[1])
                camion["precio"] = float(row[2]) 
                tipo.append(camion)
            except ValueError:
                print("Warning!")    
        return tipo

camion = leer_camion("../Data/camion.csv")
print("info dict:", camion)

from pprint import pprint
pprint(camion)

#%%
#Ejercicio 2.17

def leer_precios(nombre_archivo):
    precios = {} 
    with open(nombre_archivo, "r") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        rows = csv.reader(f) #acá defino las filas
        for row in rows: #filas definidas
            try:    
                name = row[0]
                camion["name"] = float(row[1]) 
            except IndexError:
                print("Warning!")    
        return camion

precios = leer_precios("../Data/precios.csv")
pprint(precios)
#No anda, tengo un problema para que aparezca como key el nombre de la fruta.
#%%
#Ejercicio 2.18
#Necesito usar la fc de 2.17, que no logré hacer andar.