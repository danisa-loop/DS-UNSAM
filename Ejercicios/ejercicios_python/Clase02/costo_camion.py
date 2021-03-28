# -*- coding: utf-8 -*-
#Ejercicio 2.2
with open("../Data/camion.csv", "rt") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
    headers = next(f).split(",") #separo nombres de columnas
    costo = 0 #inicializo costo en 0 ya que quiero que se vaya sumando al iterar línea a línea
    for line in f:
        row = line.split(",") #leo las líneas una a una y separo por ,
        #renombro cada item de interés según lo que corresponda y convierto a int la cantidad de cajones y a float sus precios
        cantidad = int(row[1])
        precio = float(row[2]) 
        costo += cantidad*precio #calculo el costo por cada fruta y voy sumando en c/línea de modo de acumular el total.
    print("Costo total:", costo) #imprimo afuera del for para obtener sólo el costo total
    
#%%
#Ejercicio 2.6
def costo_camion(nombre_archivo):
    with open(nombre_archivo, "rt") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        headers = next(f).split(",") #separo nombres de columnas
        costo = 0 #inicializo costo en 0 ya que quiero que se vaya sumando al iterar línea a línea
        for line in f:
            row = line.split(",") #leo las líneas una a una y separo por ,
        #renombro cada item de interés según lo que corresponda y convierto a int la cantidad de cajones y a float sus precios
            cantidad = int(row[1])
            precio = float(row[2]) 
            costo += cantidad*precio
        return costo

costo = costo_camion("../Data/camion.csv")
print("Costo total:", costo)
#%%
#Ejercicio 2.8
def costo_camion(nombre_archivo):
    with open(nombre_archivo, "rt") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        headers = next(f).split(",") #separo nombres de columnas
        costo = 0 #inicializo costo en 0 ya que quiero que se vaya sumando al iterar línea a línea
        for line in f:
            try:    #meto bloque try-except para que atrape la excepción de datos faltantes 
                row = line.split(",") #leo las líneas una a una y separo por ,
                #renombro cada item de interés según lo que corresponda y convierto a int la cantidad de cajones y a float sus precios
                cantidad = int(row[1])
                precio = float(row[2]) 
                costo += cantidad*precio
            except ValueError:
                print("Warning!")    
        return costo
        
costo = costo_camion("../Data/missing.csv")
print("Costo total:", costo)

#%% Ej. 2.9
import csv #abro archivo con módulo csv
def costo_camion(nombre_archivo):
    with open(nombre_archivo) as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        rows = csv.reader(f) #acá defino las filas
        headers = next(rows) #encabezado
        costo = 0 #inicializo costo en 0 ya que quiero que se vaya sumando al iterar línea a línea
        for row in rows: #filas definidas
            try:    
                cantidad = int(row[1])
                precio = float(row[2]) 
                costo += cantidad*precio
            except ValueError:
                print("Warning!")    
        return costo
        
costo = costo_camion("../Data/camion.csv")
print("Costo total:", costo)

#%%
#Ej. 2.11:

import csv #abro archivo con módulo csv
def costo_camion(nombre_archivo):
    with open(nombre_archivo) as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
        rows = csv.reader(f) #acá defino las filas
        headers = next(rows) #encabezado
        row = next(rows) #me quedo con la primera fila
        t = (row[0], int(row[1]), float(row[2])) #armo una tupla con los elementos de la primera fila, según el tipo que corresponda.
        costo = t[1] * t[2]
        return costo
        
costo = costo_camion("../Data/camion.csv")
print(f"{costo:0.2f}")

#%%
#Ejs. 2.12 y 2.13:
    
import csv
with open("../Data/camion.csv") as f: #Abro con with el archivo de modo de no tener que cerrarlo luego.
    rows = csv.reader(f) #acá defino las filas
    headers = next(rows) #encabezado
    row = next(rows) #me quedo con la primera fila

d = {
     'nombre' : row[0],
     'cajones' : int(row[1]),
     'precio'  : float(row[2])
    }

print(d)
cost = d["cajones"] * d["precio"]
print(cost)

d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345
print(d)

for k in d:
    print("k = ", k)
    
for k in d:
    print(k, "=", d[k])
    
items = d.items()
for k,v in d.items():
    print (k, "=", v)
#%%
#paso dict a list:
print(list(d))
#%%
nuevos_items = [('nombre', 'Manzanas'), ('cajones', 100), ('precio', 490.1), ('fecha', (13, 8, 2020))]
dic = dict(nuevos_items) #convierte lista de tuplas a diccionarios
print(dic)