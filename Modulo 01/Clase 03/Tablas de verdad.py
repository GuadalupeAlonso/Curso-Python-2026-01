# Este script demuestra las tablas de verdad para los operadores lógicos
# AND, OR y NOT en Python.

# Lista de los posibles valores booleanos que usaremos
valores_booleanos = [True, False]

# --- 1. TABLA DE VERDAD: AND (y) ---
# El operador 'and' solo devuelve True si AMBOS operandos son True.
# Piensa en ello como una condición estricta: "Necesito A Y B".

print("="*30)
print("   TABLA DE VERDAD: AND (y)")
print("="*30)
print("Regla: Solo es True si ambos son True.\n")

# Usamos dos bucles anidados para probar todas las combinaciones posibles
for a in valores_booleanos:
    for b in valores_booleanos:
        resultado = a and b
        # Usamos f-strings para formatear la salida y que se vea clara
        print(f"{a} \t and \t {b} \t = \t {resultado}")


# --- 2. TABLA DE VERDAD: OR (o) ---
# El operador 'or' devuelve True si AL MENOS UNO de los operandos es True.
# Piensa en ello como una condición flexible: "Necesito A O B".

print("\n" + "="*30)
print("    TABLA DE VERDAD: OR (o)")
print("="*30)
print("Regla: Es True si al menos uno es True.\n")

for a in valores_booleanos:
    for b in valores_booleanos:
        resultado = a or b
        print(f"{a} \t or \t {b} \t = \t {resultado}")


# --- 3. TABLA DE VERDAD: NOT (no) ---
# El operador 'not' es diferente, ya que solo opera sobre un valor.
# Simplemente invierte el resultado: lo que es True se vuelve False y viceversa.

print("\n" + "="*30)
print("    TABLA DE VERDAD: NOT (no)")
print("="*30)
print("Regla: Invierte el valor booleano.\n")

for a in valores_booleanos:
    resultado = not a
    print(f"not {a} \t = \t {resultado}")

print("\n" + "="*30)