temperatura_reactor = 198

# Ahora tenemos dos caminos posibles
if temperatura_reactor > 100:
    print("🔴 ¡ALERTA! Temperatura crítica. Activando sistema de enfriamiento.")
else:
    print("✅ Temperatura estable. Operando con normalidad.")
    print("... sistema de enfriamiento no es necesario.")