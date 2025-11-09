#Función que toma una lista y devuelva una nueva lista 
#con los elementos duplicados eliminados pero preservando el orden 
#original de la primera aparición de cada elemento

def eliminar_duplicados(lista):
    nueva_lista = []
    elementos_existentes = set()

    for elemento in lista:
        if elemento not in elementos_existentes:
            nueva_lista.append(elemento)
            elementos_existentes.add(elemento)
    return nueva_lista

lista = [1, 8 , 9, 7, 52, 78, 37, 13, 32, 2, 3, 8, 1, 44, 2, 9, 53, 54, 52, 7, 2, 1, 37, 13, 0, 1, 2, 3]
resultado = eliminar_duplicados(lista)
print(resultado)