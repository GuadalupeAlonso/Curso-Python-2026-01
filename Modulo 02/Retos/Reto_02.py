#Clases

#1. Clase Padre:
class Vehiculo:
    #Constructor:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
        self._encendido = False #protegido

    #Métodos publicos:
    def arrancar(self):
        if self._encendido == False:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El vehículo ya estaba en marcha.")

    def apagar(self):
        if self._encendido == True:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")

    def get_kilometraje(self):
        return self.kilometraje

    def mostrar_info_base(self):
        print("Información del vehículo registrado:")
        print(" - Marca:", self.marca)
        print(" - Modelo:", self.modelo)
        print(" - Año:", self.anio)

#2. Clase Hija 1:
class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def conducir(self, km):
        if self._encendido == True:
            self.kilometraje += km
            print(f"Conduciendo a {km} km...")
        else:
            print("Error: El coche debe estar arrancado para conducir.")

#3. Clase Hija 2:
class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0

    def cargar(self, kilos):
        if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
            self.__carga_actual_kg += kilos
            print("Carga exitosa.")
        else:
            print("Error: Sobrecarga.")

    def descargar(self, kilos):
        if kilos <= self.__carga_actual_kg:
            self.__carga_actual_kg -= kilos
        else:
            print("Error: No puedes descargar más de lo que hay.")

    def get_carga_actual(self):
        return self.__carga_actual_kg

#4. Codigo principal:
    #Crear objetos
mi_coche = Coche("Honda", "Civic", 2020, 4)
mi_camion = Camion("Volvo", "FH16", 2019, 5000)

#5. Prueba del coche:
print("Prueba coche:")
mi_coche.conducir(50) #intento
mi_coche.arrancar()
mi_coche.conducir(100)
mi_coche.apagar()
print(f"Kilometraje final del coche: {mi_coche.get_kilometraje()} km")

#6. Prueba del camión:
print("\nPrueba camión:")
mi_camion.cargar(3000)
mi_camion.cargar(3000) #intento
mi_camion.descargar(1000)
print(f"Carga actual del camión: {mi_camion.get_carga_actual()} kg")