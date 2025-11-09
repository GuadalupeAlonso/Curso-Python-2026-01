#Tuplas: no se pueden modificar, guardan valores estaticos
coordenadas = (10.0, 20.0)
print(coordenadas)
#pueden contener diferentes tipos de datos:
persona = ("Juan", 30, 1.75)
print(persona)
#Se accede a sus datos por medio de indices
print("Nombre: ",persona[0])
print("Edad: ",persona[1])
print("Altura: ",persona[2])
#las tuplas permiten el desempaquetado, se pueden asignar a variables
#se pueden concatenar:
tupla1=(1,2,3)
tupla2=(4,5,6)
tupla3=tupla1+tupla2
print("Tupla concatenada: ",tupla3)
#Metodo count e index
numeros = (1,2,3,4,5,6,7,8)
print("Numero de veces que aparece el 2: ", numeros.count(2))
print("Indice del primer 3: ",numeros.index(3))

#Diccionarios:
print("-"*30)
persona = {"nombre":"Ana", "edad":25, "altura":1.65} #se divide en 'clave' y 'valor'
#podemos acceder a los valores del diccionario utilizando sus claves
print("Nombre: ", persona["nombre"])
print("Edad: ",persona["edad"])
print("Altura: ", persona["altura"])
# De igual forma, podemos modificar los valores asociados a una clave
persona["edad"]=26
print("Edad actualizada: ", persona["edad"])
# para agregar nuevos pares clave-valor, simplemene asignamos un valor a una nueva clave
persona["ciudad"]="Madrid"
print("Ciudad agregada: ", persona["ciudad"])
persona["Color_Favorito"]=input("Ana, ¿cuál es tu color favorito?: ")
print("Color favorito: ", persona["Color_Favorito"])
print("-"*30)

#Metodos para manipular diccionarios
print("-"*30)
#obtener llaves del diccionario
persona = {"nombre":"Carlos", "edad":28, "ciudad":"Barcelona"}
claves = persona.keys()
print("Claves del diccionario: ",claves)
#obtener valores del diccionario
valores=persona.values()
print("Valores del diccionario: ", valores)
#permite acceder al valor asociado a una clave
print("Pares clave-valor del diccionario: ", persona.items())
print("-"*30)
print("Edad usando get(): ", persona.get("edad"))
# pop() elimina el par clave-valor asociado a una clave y devuelve su valor
edad_eliminada = persona.pop("edad")
print("Edad eliminada: ", edad_eliminada)

#Anidar diccionarios:
#1. empezamos con el archivo vacio
base_de_datos = {}
#2. creamos el primer expediente (diccionario anidado)
nuevo_usuario = {
    "nombre":"Elena Garza",
    "edad":42,
    "email":"elena.g@email.com"
}
#3. lo guardamos en el archivador con su clave unico
base_de_datos["user_103"]=nuevo_usuario
#4. tambien puedes hacerlo directamente:
base_de_datos["user_104"]={
    "nombre":"Juan Perez",
    "edad":22,
    "email":"juan.p@email.com"
}
print(base_de_datos)
#para acceder a los datos anidados
print("Nombre del user_103: ", base_de_datos["user_103"]["nombre"])
#para modificar un valor en un diccionario anidado:
base_de_datos["user_104"]["edad"]=23
print("Edad actualizada del user_104: ",base_de_datos["user_104"]["edad"])
#para agregar un uevo par clave-valor a un diccionario anidado:
base_de_datos["user_103"]["telefono"]="555-1234"
print("Telefono agregado al user_103: ",base_de_datos["user_103"]["telefono"])
print("-"*30)
#se puede iterar sobre los diccionarios anidados utilizando bucles:
#separamos sobre listas, en la primer lista se separada el id, y en la segunda una lista con los clave-valor de la informacion del usuario
for user_id, user_info in base_de_datos.items(): #items para obtener clave y valor
    print(f"ID de usuario: ",{user_id})
    for clave, valor in user_info.items(): #iteramos sobre el diccionario anidado
        print(f" {clave}: {valor}")

#Funcion set: almacena datos, no se pueden repetir, no tienen orden en especial
conjunto1 = {1,2,3,4,5}
print("Conjunto 1: ",conjunto1)
conjunto2=set(["a","b","c","d"])
print("Conjunto 2: ",conjunto2)
#Ventajas: elimina automaticamente elementos duplicados
#Metodos para manipular sets:
conjunto1.add(6) #agrega
conjunto1.remove(3) #remueve, si no lo encuentra envia error
conjunto1.discard(10) #descarta, si no lo encuentra, no pasa nada
conjunto_union=conjunto1.union({7,8,9})
conjunto_interseccion=conjunto1.intersection({4,5,6,7})
conjunto_diferencia = conjunto1.difference({4,5})
conjunto1.clear()

#Diferencias conjuntos de datos:
#Listas: son mutables, se pueden acceder a sus datos, se pueden agregar datos, etc
#Tuplas: son inmutables, no se pueden agregar datos, se pueden obtener los datos que contiene pero no se pueden operar, no se pueden limpiar
#Diccionarios: clave-valor
#Sets: los elementos que contiene no se pueden repetir

#Ejemplo sets:
print("Uso practico de sets:")
prototipo_1_componentes={"motor", "ruedad", "chasis", "bateria"}
prototipo_2_componentes={"motor", "aleron", "chasis", "computadora"}
#union 
todos_los_elementos = prototipo_1_componentes.union(prototipo_2_componentes)
print(f"Union: {todos_los_elementos}")
#interseccion
componentes_comunes=prototipo_1_componentes.intersection(prototipo_2_componentes)
print(f"Interseccion: {componentes_comunes}") 
#diferencia
solo_en_proto_1=prototipo_1_componentes.difference(prototipo_2_componentes)
print(f"Solo en 1: {solo_en_proto_1}")
print("-"*30)
#los sets se usan cuando el orden no importa y la unicidad sí
#para eliminar duplicados, para comparar dos listas y ver que tienen en comun


#Modulos en python: archivos que contienen codigo en python (funciones, clases, etc)
#pueden ser reutilizados en otros programas
from os import system
system("cls") #limpiamos la consola (solo en windows)
print("-"*30)
import math #importamos la libreria matematica
#para usar sus funciones, usamos el formato: libreria.funcion()
area_circulo = math.pi * (10 ** 2)
raiz_cuadrada=math.sqrt(64)
print(f"La raiz de 64 es: {raiz_cuadrada}")
print(f"El área es: {area_circulo}")
print("-"*30)
#otra manera de importar modulos es usando from ... import
from random import randint, choice
numero_suerte= randint(1,100) #un numero aleatorio entre 1 y 100
premios = ["Auto", "Casa", "Viaje", "Nada"]
tu_premio=choice(premios) #elige un elemento aleatorio de la lista
print(f"Tu numero de la suerte es: {numero_suerte}")
print(f"¡Ganaste: {tu_premio}!")
print("-"*30)
