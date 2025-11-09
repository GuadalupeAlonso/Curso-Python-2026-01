#Perfil de datos:
from datetime import datetime #para conocer el año actual
#Nombre y año de nacimiento
nombre = input("¿Cuál es tu nombre?: ")
nacimiento = int(input("¿Cuál es tu año de nacimiento?: "))
#Tres videojuegos favoritos
videojuegos = input("Escribe tus tres videojuegos favoritos (separados por comas): ").lower()
#Lista perfil
lista_perfil = [nombre]
#Edad del usuario
año_actual = datetime.now().year
edad_usuario = año_actual - nacimiento
lista_perfil.append(edad_usuario)
#Agregar videojuegos a lista
lista_videojuegos = videojuegos.split(",") #separa la respuesta del usuario en 3 strings por medio de la coma
for i in range(1, 3): #aplica para el indice 1 y 2 unicamente
    lista_videojuegos[i] = lista_videojuegos[i].replace(" ", "")
lista_perfil.extend(lista_videojuegos) #agrega los elementos de lista_videojuegos a lista_perfil, no se puede hacer con append pq lo agrega solo como el indice 2
#Usuario activo 
activo = True
lista_perfil.insert(0,activo) #se inserta en el indice 0
#El primer videojuego favorito y se elimina de la lista
juego_favorito = lista_perfil[3].capitalize()
lista_perfil.pop(3)
#Comprobar si es mayor de edad
if edad_usuario >= 18:
    mayor_de_edad = True
else:
    mayor_de_edad = False
#Comprobar si nombre mayor a 10 caracteres
if len(nombre) > 10:
    nombre_largo = True
else:
    nombre_largo = False
#Comprobar si es gamer retro
if "pacman" in lista_perfil:
    gamer_retro = True
else:
    gamer_retro = False
#Impresión final
print(f"\nBienvenid@, {lista_perfil[1]}")
if activo == True:
    print(f"Usuario activo")
else:
    print("Estas desconectado del portal...")
if mayor_de_edad == True:
    print("Por ser mayor de edad cuentas con permiso para entrar al portal...")
    print("Por lo que conoceras tu perfil gamer:")
    print(f"1. Tu juego favorito es: {juego_favorito}")
    if nombre_largo == True:
        print("Sugerencia: cuentas con un nombre de usuario demasiado largo para el portal...")
        print("Te recomendamos cambiarlo lo antes posible, si no tu suscripción se cancelará después de los próximos 3 días.")
    else:
        pass
    if gamer_retro == True:
        print("2. Además, te consideramos parte de nuestra comunidad gamer retro...")
        print("   Felicidades por este logro!!!")
    else:
        print("\nEsta es toda la información con la que contamos por el momento...")
else:
    print("No cuentas con permiso de entrar al portal.")