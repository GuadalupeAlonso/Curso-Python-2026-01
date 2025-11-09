#sentencia de control IF
#la condicional if nos permite tomar desiciones de acuerdo a una condición
#Para que la condicional funcione se requiere al menos una variable
# Programa que evalúa la temperatura de un reactor
temperatura_reactor = 1

# La primera regla: ¿supera el límite crítico?
if temperatura_reactor > 100:
    print("🔴 ¡ALERTA! Temperatura crítica. Activando sistema de enfriamiento.")
    print("... sistema de enfriamiento activado.")
temperatura_reactor = int(input("Introduce la nueva temperatura del reactor: "))
print("La nueva temperatura del reactor es:", temperatura_reactor)