# -*- coding: utf-8 -*-
#Ej. 2.14:
    
def geringoso(list):
    t = []
    ger = ""
    vocales = "aeiou"
    for e in list:
        for i in e:
            if i in vocales:
                ger += i + "p" + i
            else:
                ger += i
        ger
        tup = (e, ger)
        t.append(tup)  
    return t
        
lista = ["banana", "manzana", "mandarina"]
print(geringoso(lista))
#La primera tupla da bien, en las siguientes concatena la palabra anterior al escribirla en geringoso
#%%
def geringoso(list):
    d = {}
    ger = ""
    vocales = "aeiou"
    for e in list:
        for i in e:
            if i in vocales:
                ger += i + "p" + i
            else:
                ger += i
            ger
        d[e] = ger
    return d
        
lista = ["banana", "manzana", "mandarina"]
print(geringoso(lista))
#ídem arriba