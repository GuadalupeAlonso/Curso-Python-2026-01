import json
import statistics # (Día 8)

ARCHIVO_JSON = "mi_base_de_datos.json"

print("Iniciando carga de base de datos...")
try:
    with open(ARCHIVO_JSON, "r") as f:
        # ¡La magia! Carga el archivo 'f' y lo traduce a un dict
        db_cargada = json.load(f)
        
    print("✅ ¡Base de datos cargada!")

    # ¡'db_cargada' ES un diccionario de Python!
    # Podemos usar todo lo que ya sabemos (Día 7)
    
    print("\n--- Reporte de Alumnos Cargados ---")
    for id_alumno, datos in db_cargada.items():
        nombre = datos["nombre"]
        califs = datos["calificaciones"] # Esto es una LISTA (Día 3)
        
        # (Integrando Día 8 y 9)
        promedio = statistics.mean(califs)
        print(f"ID: {id_alumno} | Nombre: {nombre} | Promedio: {promedio:.2f}")

except FileNotFoundError:
    print(f"ℹ️ El archivo '{ARCHIVO_JSON}' no existe. Se creará uno nuevo al guardar.")
    db_cargada = {} # Empezamos con un dict vacío
except json.JSONDecodeError:
    print(f"❌ ERROR: El archivo '{ARCHIVO_JSON}' está corrupto o vacío. Empezando de cero.")
    db_cargada = {} # Empezamos con un dict vacío

except Exception as e:
    print(f"❌ Ocurrió un error inesperado: {e}")
    db_cargada = {}
    
# Ahora 'db_cargada' contiene nuestros datos, ya sea cargados o vacíos