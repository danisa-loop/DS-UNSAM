# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:46:52 2021

@author: hao_1
"""


cadena = 'boligoma'
for c in cadena:
    if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        a = cadena.replace("a", "apa")
        e = a.replace("e", "epe")
        i = e.replace("i", "ipi")
        o = i.replace("o", "opo")
        u = o.replace("u", "upu")
print(u)