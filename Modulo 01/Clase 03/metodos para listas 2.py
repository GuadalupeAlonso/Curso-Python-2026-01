lista = [1, 2, 3]
#metodo .len() para obtener la longitud de una lista
print(f"Longitud de la lista: {len(lista)}")
#metodo .sort() para ordenar los elementos de una lista
lista_numeros = [3, 1, 4, 2]
print(f"Lista desordenada: {lista_numeros}")
lista_numeros.sort() #ordena la lista en orden ascendente
print("Lista ordenada:", lista_numeros)
#metodo .reverse() para invertir el orden de los elementos de una lista
lista_numeros.reverse()
print("Lista invertida:", lista_numeros)
#metodo .count() para contar cuantas veces aparece un elemento en una lista
lista_duplicados = [1, 2, 2, 3, 3, 3]
print(f"Lista con duplicados: {lista_duplicados}")
print("El numero 2 aparece", lista_duplicados.count(1), "veces")
print("El numero 3 aparece", lista_duplicados.count(3), "veces")