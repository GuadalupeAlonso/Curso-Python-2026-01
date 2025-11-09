#Ciclo while
bandera = True 
while bandera:
    print("El ciclo while se esta ejecutando: ")
    #aqui se puede poner una condición
    respuesta = input("¿Deseas continuar (s/n)?: ")
    if respuesta.lower() != 's':
        bandera = False
print("El ciclo while ha terminado")

#ciclo while controlado:
#while se ejecutara hasta que una condicion cambie
#for se ejecuta por medio de un rango 
contador = 1
suma = 0
while contador <= 5:
    numero = int(input("Ingrese un numero: "))
    suma += numero
    contador += 1
    print(f"Has ingresado {contador - 1 } numeros.")
print("La suma de los numeros ingresado es: ",suma)

#break y continue en for:
#la instrucción break se utiliza para salir de un bucle antes de que haya terminado
for numero in range(10):
    if numero == 5:
        break #sale del bucle cuando numero es igual a 5
    print(numero)
print("Bucle terminado con break")
print("-"*20)
#La instrucción continue se utiliza para saltar la iteración actual y pasar a la siguiente
for numero in range(10):
    if numero % 2 == 0:
        continue #salta los numeros pares
    print(numero)
print("Bucle terminado con continue")

#Ejemplo:
contador = 0
while contador < 10:
    contador += 1
    if contador == 7:
        break #salir del bucle cuando contador es igual a 7
    if contador % 2 == 0:
        continue #salta los numeros pares
    print(contador)

#Ejemplo 2:
while True:
    entrada = input("Escribe 'salir' para terminar el bucle: ")
    if entrada.lower() == 'salir':
        break #sale del bucle si el usuario escribe 'salir'
    print(f"Has escruto: {entrada}")
print("Bucle terminado con greak y continue en while")

#Cuándo se usa el ciclo while y cuando for?
#La diferencia entre ciclo for y ehile es que el ciclo for siempre se usa para rangos
#while es cuando no sabemos cuántas veces se repite el ciclo, como con entradas de usuario, o cuando no sabemos si el usuario se va a equivocar o no

#Ciclo for: cuando se conoce el numero de iteraciones o se itera sobre una secuencia 
print("Contaremos los numero divisibles entre 5 en un rango del 1 al 100:")
for numero in range(1,101):
    if numero % 5 == 0:
        print(numero)
print(f"Hay {100//5} numeros divisibles entre 5 en un rango del 1 al 100")

#Ciclo while: cuando no se sabe cuantas veces se repetira el bloque de codigo y depende de una condicion 
numero_secreto = 5
numero_intentos = 1
while True:
    intentos = int(input("¿En qué numero estoy pensando?: "))
    if intentos < 1 or intentos > 10:
        print("Bobo, el numero debe estar entre 1 y 10.")
        numero_intentos += 1
        continue
    elif intentos == numero_secreto:
        print("Correcto. El numero que estaba pensando era el: ", numero_secreto)
        break
    else:
        print("Error, llevas ", numero_intentos, "intentos, intenta de nuevo.")
        numero_intentos += 1
print("Juego terminado, lo lograste en ", numero_intentos, "intentos.")


#Manejo de errores de errores y excepciones
try:
    numero = int(input("Ingresa un número entero: "))
    resultado = 10 / numero
    print(f"El resultado de 10 dividio por {numero} es {resultado}")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")
except ValueError:
    print("Error: debes ingresar un numero entero valido")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")
print("Programa terminado.")

#Uso de errores y excepciones en ciclos
print("Validador de edad:")
while True:
    try:
        # 1. Intentamos ejecutar este codigo_
        edad_str = input("Introduce tu edad: ")
        edad_int = int(edad_str)

        #Si llegamos aqui, la conversion fue exitosa:
        print(f"Correcto, tu edad es {edad_int}")
        break #salimos del bucle while
    
    except ValueError:
        # 2. Si el try falla (porque no puedo hacer int())
        #el programa salta aqui en lugar de crashear
        print("Error: '{edad_str}' no es un numero valido. Intenta de nuevo.")
print("Programa terminado.")

#Manejo de errores en listas:
inventario = ["Poción", "Espada", "Escudo"]
print("Indices disponibles: 0, 1, 2")
while True:
    try:
        # 1. Intentamos obtener el indice
        indice_str = input("¿Qué indice de item quieres inspeccionar?: ")
        indice = int(indice_str)
        # 2. Intentamos usar el indice
        print(f"Has seleccionado: {inventario[indice]}")
    # Podemos anidar excepciones para entregar diferentes errores
        break #salimos del bucle si todo salió bien
    except ValueError:
        print("Error: Debes introducir un número (0, 1 o 2)")
    except IndexError:
        # 3. Si el 'int()' funcionó pero el indice estaba fuera de rango
        print(f"Error: Ese indice no existe. Solo tienes {len(inventario)} items.")
