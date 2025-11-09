# 1. Funciones
```python
print("Hola mundo")
```
# 2. Comentarios
```python
# Comentario sencillo
"""
Bloque de comentarios
"""
```
# 3. Variables
```python
entero = 10 #int
flotante = 10.5 #float
cadena = "Hola" #str
booleano = True #bool
lista = [1,2,3] #list
tupla = (1,2,3) #tuple
conjunto = {1,2,3} #set
```

# 4. Función type

Regresa el tipo de variable
```python
print(type(entero))   #<class 'int'>
print(type(flotante)) #<class 'float'>
```

# 5. Conversión de variables
```python
a = 5
b = 2.0
c = "3"
print(a+b+int(c))
# Se convierte el caracter "3" en numero para poder procesar la suma
print(a+b+float(c))
print(str(a)+str(b)+c) #Resultado: 52.03, solo combinó las 3 cifras como str
```

# 6. Nombre de variables
```python
#Nombres aceptables:
nombre_variable = "valor"
nombreVariable = "valor"
```

# 7. Formas de interactuar con el usuario
```python
#Función input: devuelve un str
print("Hola usuario, por favor ingresa tu nombre")
nombre = input()
print("Hola, "+ nombre + "bienvenido a Python")
```

```python
#Otra forma de usar input
nombre = input("Por favor ingresa tu nombre")
print("Hola, "+ nombre + "bienvenido a Python")
```

```python
#Función print
print("Hola usuario, por favor ingresa tu nombre")
nombre = input()
```

```python
#Función print f
print(f"Hola {nombre}, bienvenido a python")
```

```python
#Si queremos que ingrese un numero tenemos que convertir el str de input a numero
edad = int(input("Por favor ingresa tu edad: "))
print(f"Tu edad es {edad} años")
```

# Reto del día

![[Captura de Pantalla 2025-10-13 a la(s) 17.00.08.png]]
