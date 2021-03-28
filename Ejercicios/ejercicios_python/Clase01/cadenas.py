print("Ejercicio 1.17:")
 
cadena = "Ejemplo con for"
print(cadena) 

#Cantidad de letras o en cadena
suma = 0   
for c in cadena:
    if "o" in c:
        suma = suma + 1
        
print("hay", suma, "letras o en", cadena)
