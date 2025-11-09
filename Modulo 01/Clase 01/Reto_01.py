#Reto 13/10/25
print("Hola, por favor contesta la siguiente encuesta")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ahora ingresa tu edad (unicamente los números): "))
frase_fav = input("Comparte tu frase favorita: ")
dinero_dispo = float(input("¿Cuánto dinero tienes disponible en el banco? $"))

print("De acuerdo a tus respuestas esto es lo que aprendí sobre ti...")
print(f"Tu nombre es {nombre}, tienes {edad} años, tu frase favorita es '{frase_fav}'; \n y cuentas con ${dinero_dispo} MXN en el banco")