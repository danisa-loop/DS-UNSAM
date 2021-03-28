frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
print(frutas)
lista_frutas = frutas.split(",") #Convierte la cadena de caracteres fruta a una lista
print(lista_frutas)
lista_frutas[2] = 'Granada'
print("Modifiqué el elemento 3 de la lista original, entonces la nueva lista queda: ", lista_frutas)