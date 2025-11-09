#metodos para listas
#¿Que es un metodo? Una funcion que esta asociada a un objeto
#metodo .append() para agregar un elemento al final de una lista
lista = [1, 2, 3]
print(lista)
lista.append(76)
print(lista)
#metodo .remove() para eliminar un elemento de una lista
lista.remove(2) #elimina la primera ocurrencia del valor 2
print(lista)
#metodo .pop() para eliminar un elemento de una lista por su indice
elemento_eliminado = lista.pop(0) #elimina el elemento en el indice 0
print("Elemento eliminado:", elemento_eliminado)
print("Lista despues de pop:", lista)
#metodo .insert() para insertar un elemento en una posicion especifica
lista.insert(1, 10) #inserta el valor 10 en el indice 1
print("Lista despues de insert:", lista)
lista_duplicados = [1, 2, 2, 3, 3, 3]
lista_duplicados.clear()
print("Lista despues de clear:", lista_duplicados)
#metodo .extend() para agregar los elementos de una lista a otra lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print("Lista1 despues de extend:", lista1)

