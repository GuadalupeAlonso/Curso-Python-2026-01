#Función que recibe una cadena de texto y devuelve un diccionario 
# donde las claves sean las palabras y los valores sean la cantidad 
# de veces que aparece cada palabra

import string

def contar_palabras_archivo(archivo_entrada, archivo_salida):
    #Leer el archivo:
    with open(archivo_entrada, "r", encoding="utf-8") as f:
        texto = f.read()
    texto = texto.lower() #convertir a minúsculas
    #Eliminar puntuación:
    for signo in string.punctuation + "¿¡«»…“”":
        texto = texto.replace(signo, " ")

    palabras = texto.split() #separar palabras
    #Contar palabras:
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    #Lista de palabras a guardar
    palabras_interes = [
        "dostoievski",
        "sinónimos",
        "horiki",
        "humanos",
        "miedo",
        "palabras"
    ]

    #Guardar conteo:
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for palabra in palabras_interes:
            cantidad = conteo.get(palabra, 0)
            f.write(f"{palabra}: {cantidad}\n")

contar_palabras_archivo("Entrada.txt", "Conteo_palabras.txt")