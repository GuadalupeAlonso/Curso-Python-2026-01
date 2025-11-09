#Calculadora:
print("Calculadora (:")
print("Ingresa dos números para comenzar:")
a=int(input("a = "))
b=int(input("b = "))
#Suma de dos numeros
print(f"La suma de {a} + {b} es: ", a+b)
#Resta de dos numeros
print(f"La resta de {a} - {b} es: ", a-b)
#Multiplicacion de dos numeros
print(f"La multiplicación de {a} * {b} es: ", a*b)
#División de dos numeros
print(f"La división de {a} / {b} es: ", round(a/b,2))
#Modulo 2 de a y b
print(f"El módulo 2 de {a} es: ", a%2)
print(f"El módulo 2 de {b} es: ", b%2)
#Potencia cubica de a y b
print(f"La potencia cúbica de {a} es: ", a**3)
print(f"La potencia cúbica de {b} es: ", pow(b,3))

print("-"*50)

print("Calculadora 2 (:")
print("Ingresa dos números diferentes a los anteriores:")
c=int(input("c = "))
d=int(input("d = "))
#Asignación suma
print(f"La asignación suma de {c} += 2 es: {c+2}. La asignación suma de {d} += 2 es: {d+2}")
#Asignación resta:
print(f"La asignación resta de {c} -= 13 es: {c-13}. La asignación resta de {d} -= 13 es: {d-13}")
#Igualdad
print(f"Igualdad: \n{c} es igual a {d}: ",c==d)
#Desigualdad
print(f"Desigualdad: \n{c} es desigual a {d}: ",c!=d)
#Mayor que
print(f"Mayor que: \n{c} es mayor que {d}: ",c>d)
print(f"{d} es mayor que {c}: ",d>c)
#Mayor que
print(f"Menor que: \n{c} es menor que {d}: ",c<d)
print(f"{d} es menor que {c}: ",d<c)

print("-"*50)

print("Tablas de verdad (:")

print("Tabla de verdad de compuerta AND:")
print("-"*7)
print("|A|B|x|")
print("-"*7)
print(f"|0|0|{0 and 0}|")
print("-"*7)
print(f"|0|1|{0 and 1}|")
print("-"*7)
print(f"|1|0|{1 and 0}|")
print("-"*7)
print(f"|1|1|{1 and 1}|")
print("-"*7)

print("Tabla de verdad de compuerta OR:")
print("-"*7)
print("|A|B|x|")
print("-"*7)
print(f"|0|0|{0 or 0}|")
print("-"*7)
print(f"|0|1|{0 or 1}|")
print("-"*7)
print(f"|1|0|{1 or 0}|")
print("-"*7)
print(f"|1|1|{1 or 1}|")
print("-"*7)

print("Tabla de verdad de compuerta NOT:")
print("-"*7)
print("|A|x|")
print("-"*7)
print(f"|0|{int(not 0)}|")
print("-"*7)
print(f"|1|{int(not 1)}|")
print("-"*7)