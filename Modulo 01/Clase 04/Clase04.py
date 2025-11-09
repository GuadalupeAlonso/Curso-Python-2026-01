#Metodo para operar strings
cadena=input("Escribe una cadena de texto: ")
print("La cadena en mayusculas es: ", cadena.upper())
print("La cadena en minusculas es: ", cadena.lower()) 
print("La cadena con la primera letra en mayusculas es: ", cadena.capitalize()) 
print("La cadena con cada palabra iniciando en mayusculas es: ", cadena.title())
print("La cadena con las vocales en mayuscula es: ", cadena.replace("a","A").replace("e","E").replace("i","I").replace("o","O").replace("u","U"))
print("La cadena con espacios eliminados al inicio y al final es: ", cadena.strip())
print("La cadena con espacios eliminados al inicio es: ",cadena.lstrip())
print("La cadena con espacios eliminados al final es: ", cadena.rstrip())

#Sentencia de control: if
temperatura_reactor = 105
#La primera regla: ¿supera el limite critico?
if temperatura_reactor > 100:
    print("¡ALERTA! Temperatura critica. Activando sistema de enfriamiento")
print("... el programa continua su ejecución normal.")

#Else: Ahora tenemos dos caminos posibles:
temperatura_reactor_2 = 98
if temperatura_reactor_2 > 100:
    print("¡ALERTA! Temperatura critica. Activando sistema de enfriamiento")
else:
    print("Temperatura estable. Operando con normalidad.")

#Elif: evita anidar demasiados if's
#El usuario introduce un valor de rpm
rpm = int(input("Introduce las rpms actuales del motor: "))

if rpm > 2500:
    print("PELIGRO: Velocidad excesiva. Reduciendo potencia.")
elif rpm > 1800:
    print("PRECAUCIÓN Velocidad alta. Revisar carga de trabajo.")
elif rpm > 600:
    print("OPTIMO. Velocidad de crucero. Operando eficientemente.")
elif rpm > 0:
    print("INFORMATIVO: Motor a baja velocidad.")
else:
    print("Motor detenido.")

#If anidado:
#las desiciones rara vez son lineales, es decir a partir de una desicion se puede tomar otra desición
#una desicion que lleva a un conjunto de desiciones se llama desicion anidada
# Variables que simulan los sensores del dron
bateria_porcentaje = 85
motor_activo = True
altitud_metros = 60
print("Iniciando el programa diagnostico del dron...")
bateria_porcentaje = int(input("Dime el porcentaje de bateria que tiene tu dron: "))
motor_activo = input("El motor esta activo? (si/no): ")
if motor_activo.lower() == "si":
    motor_activo = True
else:
    motor_activo = False
altitud_metros = int(input("Dime la altitud en metros a la que esta volando el dron"))
print("--- Iniciando diagnóstico del Dron ---")

# --- PRIMER NIVEL DE DECISIÓN: ¿Hay suficiente batería? ---
if bateria_porcentaje > 20:
    print(f"✅ Batería OK ({bateria_porcentaje}%)")

    # --- SEGUNDO NIVEL DE DECISIÓN: ¿Están los motores activos? ---
    # Este bloque 'if/else' está ANIDADO dentro del primer 'if'.
    # Solo se ejecuta si la batería está OK.
    
    if motor_activo == True:
        print("  ✅ Motores Activos.")

        # --- TERCER NIVEL DE DECISIÓN: Evaluar la altitud de vuelo ---
        # ¡Podemos anidar aún más profundo!
        
        if altitud_metros > 100:
            print(f"  🔴 ALERTA: Altitud excesiva ({altitud_metros}m). Descendiendo.")
        elif altitud_metros > 50:
            print(f"  🟡 PRECAUCIÓN: Altitud elevada ({altitud_metros}m). Manteniendo posición.")
        else:
            print(f"  ✅ Altitud segura ({altitud_metros}m).")

    else: # else del segundo nivel
        print("  🟡 ALERTA: Batería OK, pero los motores están inactivos.")

else: # else del primer nivel
    print(f"🔴 CRÍTICO: Batería baja ({bateria_porcentaje}%). Imposible despegar. Aterrizando de emergencia.")

print("--- Diagnóstico Finalizado ---")

#Diferencia entre if's anidados y elif, es cuando la sentencia siguiente no tiene que ver con la otra (elif)
#cuando sí, se utiliza if's anidados. 

