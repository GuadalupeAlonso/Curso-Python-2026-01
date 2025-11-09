# El usuario introduce la velocidad de un motor en RPM
rpm = int(input("Introduce las RPM actuales del motor: "))

# Inspección completa con múltiples condiciones
if rpm > 2500:
    print("🔴 PELIGRO: Velocidad excesiva. Reduciendo potencia.")
elif rpm > 1800:
    print("🟡 PRECAUCIÓN: Velocidad alta. Revisar carga de trabajo.")
elif rpm > 600:
    print("✅ ÓPTIMO: Velocidad de crucero. Operando eficientemente.")
elif rpm > 0:
    print("🔵 INFORMATIVO: Motor a baja velocidad (ralentí).")
else:
    print("⚪️ Motor detenido.")