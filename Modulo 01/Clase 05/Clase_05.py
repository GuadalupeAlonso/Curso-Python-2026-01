#Ciclos de control
secuencia = [1,2,3,4,5]
#Para imprimir todos los elementos de una lista:
#No es necesario declarar variables, ni definir las iteraciones para el for
for elemento in secuencia:
    print(elemento)

#funcion range
print("Iniciando prueba de 5 ciclos del motor: ")
# i: indice es esl nombre estandar para contadores
for i in range(5): #range genera una lista en automatico de forma superficial
    print(f"Ciclo de prueba número {i+1}") #usamos i+1 para que cuente 1,2,3,4,5
    #si quieremos un rango especifico, podemos indicarlo en la funcion range

print("\nProbando ciclos del motor del 3 al 7: ")
for i in range(3,8):
    print(f"Ciclo de prueba numero {i}")

#Tambien podemos indicar un paso diferente de 1 en 1 
print("\nProbando ciclos del motor del 2 al 10, de 2 en 2: ")
for i in range(2,11,2): #empieza en 2, termina en 11 y va de 2 en 2 
    #tenemos que definir un numero despues del que queremos llegar considerando que las listas empiezan a contarse desde posicion 0 y no 1
    print(f"Ciclo de prueba número {i}")

#Ejemplo practico para usar for y range:
for numero in range(1,11):
    print(f"El numero es: {numero}")
#Este script imprime los numeros del 1 al 10 utilizando un bucle for y la funcion range
# la funcion range(1,11) genera una secuencia de numeros desde 1 hasta 10 (el 11 no)
materiales=["acero","madera","plastico"]
for material in materiales:
    print(f"El material es: {material.capitalize()}")

#Ejemplo acumuladores:
mediciones_voltaje = [12.5,12.1,12.7,12.4,12.6]
suma_total=0.0 #creamos el acumulador afuera del bucle

for voltaje in mediciones_voltaje:
    #actualizamos el acumulador dentro dle bucle
    suma_total=suma_total+voltaje
    print(f"Sumando {voltaje}... Suma parcial: {suma_total}")
    #Al final del for la variable voltaje se quedara con el ultimo valor de la lista

#Hacemos el resultado fuera del bucle:
cantidad_mediciones = len(mediciones_voltaje) #sacamos la cantidad de datos que hay en la lista
promedio = suma_total/cantidad_mediciones
print(f"\nReporte final:")
print(f"Suma total de voltajes: {suma_total}V")
print(f"Promedio de voltaje: {promedio:.2f}V")

#Ciclos anidados:
for i in range(1,4): #Ciclo externo
    print(f"Ciclo externo i={i}")
    for j in range(1,4): #ciclo interno
        print(f"Ciclo interno j={j}")
    print() #linea en blanco para separar iteraciones del ciclo externo

#Ejemplo de anidamiento de ciclos
temperaturas = [50,70,100]
presiones = [10,20]
print("--- Iniciando Simulación de Pruebas de Material ---")
# --- BUCLE EXTERIOR (Controla la temperatura) ---
# Se ejecutará 3 veces
for temp in temperaturas:
    
    print(f"\n--- Pruebas a {temp}°C ---")

    # --- BUCLE INTERIOR (Controla la presión) ---
    # Por CADA temperatura, este bucle se ejecutará 2 veces
    for pres in presiones:
        
        # Este código se ejecuta 3 * 2 = 6 veces
        print(f"  Ejecutando prueba: {temp}°C y {pres} psi...")
        # (Aquí iría el código de la simulación)
print("\n--- Simulación Finalizada ---")

#Combinar sentencias if con bucles for:
mediciones_ph = [7.1,7.3,6.4,7.0,7.6,7.2,5.9]
conteo_anomalias=0
anomalias_detectadas=[]

print("\nIniciando monitor de calidad de ph...")
for ph in mediciones_ph:
    #Este "if" se ejecuta en cada iteracion
    if ph < 6.5 or ph > 7.5:
        print(f"Alerta: Se detectó valor anómalo: {ph}")
        conteo_anomalias=conteo_anomalias+1
        anomalias_detectadas.append(ph)

print("---Analisis de calidad completo---")
print(f"Total de anomalias registradas: {anomalias_detectadas}")
print(f"Total de anomalías: {conteo_anomalias}")
print(f"Valores anómalos registrados: {anomalias_detectadas}")