#Ejercicio práctico 
#Vamos a pedir al usuario que nos de sus datos: Nombre, edad, una frase favorita y cuanto dinero tiene
#Despues vamos a imprimir estos datos
#y le vamos a decir cuantos años tendra en 10 años
#y cuanto dinero tendra si le damos 1000 mx mas
nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
frase_favorita = input("Dame tu frase favorita: ")
dinero = float(input("Cuanto dinero tienes? "))
print("Tu nombre es: ", nombre)
print("Tu edad es: ", edad)
print("Tu frase favorita es: ", frase_favorita)
print("Tu dinero es: ", dinero)
print("En 10 años tendras: ", edad + 10)
print("Si te doy 1000 mas, tendras: ", dinero + 1000)
print(f"Hola {nombre}, tu frase favorita es '{frase_favorita}'. En 10 años tendras {edad + 10} años y si te doy 1000 mas, tendras {dinero + 1000} pesos.")