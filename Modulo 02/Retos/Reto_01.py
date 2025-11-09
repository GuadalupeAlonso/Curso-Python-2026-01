#Reportes

#1. Definir clase
class Componente:
#2. Crear constructor
    def __init__(self, numero_serie, tipo_componente, costo):
        self.numero_serie = numero_serie
        self.tipo = tipo_componente
        self.costo = costo
        self.historial_revisiones = []
        self.esta_activo = True
#3. Crear objetos
c1 = Componente("MTR-1001", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)

#4. Interactuar con atributos
c1.historial_revisiones.append("2025-10-25")
c1.historial_revisiones.append("2025-11-09")
c2.esta_activo = False

#5. Imprimir reporte
print("Reporte del Componente 1 registrado:")
print(" - Número de serie:", c1.numero_serie)
print(" - Tipo de componente:", c1.tipo)
print(" - Costo del componente: $", c1.costo)
print(" - Historial de revisiones:", c1.historial_revisiones)
print(" - Estado activo:", c1.esta_activo)

print("\nReporte del Componente 2 registrado:")
print(" - Número de serie:", c2.numero_serie)
print(" - Tipo de componente:", c2.tipo)
print(" - Costo del componente: $", c2.costo)
print(" - Historial de revisiones:", c2.historial_revisiones)
print(" - Estado activo:", c2.esta_activo)
