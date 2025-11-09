#Análisis de las calificaciones de un curso
print("\nSistema de registro de calificaciones...")
#Solicitar cantidad de alumnos
cantidad_alumnos = int(input("\nIngresa la cantidad de alumnos que están registrados en el curso: "))
#Solicitar alumnos y calificaciones
print("Registro de calificaciones...")
lista_alumnos = []
lista_calificaciones = []
for alumnos in range(cantidad_alumnos):
    nombres = input("Ingresa el nombre del alumno: ").strip() #elimina los espacios en blanco al principio y al final de cada string
    lista_alumnos.append(nombres)
    calificaciones = round(float(input("Ingresa su calificación: ").replace(" ", "")),2) #redondea el numero a dos decimales
    lista_calificaciones.append(calificaciones)
#Clasificación de alumnos por aprobados, reprobados y excelentes; y promedio general del grupo
aprobados = []
reprobados = []
excelentes = []
suma_calificaciones = 0
for i in range(cantidad_alumnos):
    nombre_alumno = lista_alumnos[i] #cada nombre de cada alumno
    calificacion_alumno = lista_calificaciones[i] #cada calificacion de cada alumno
    suma_calificaciones += calificacion_alumno
    #Clasificacion alumnos
    if calificacion_alumno < 5.99:
        reprobados.append((nombre_alumno,calificacion_alumno))
    elif calificacion_alumno >= 6 and calificacion_alumno <= 9.99:
        aprobados.append((nombre_alumno,calificacion_alumno))
    else:
        excelentes.append((nombre_alumno,calificacion_alumno))
promedio_general = suma_calificaciones / cantidad_alumnos 
#Impresión final:
print("\nResumen del registro...")
print(f"En el grupo registrado se clasificaron {cantidad_alumnos} alumnos.")
print(f"El promedio general del grupo es: {promedio_general:.2f}")
print(f"La calificación más alta del grupo es: {max(lista_calificaciones)}")
print(f"La calificación más baja del grupo es: {min(lista_calificaciones)}")
print(f"Los alumnos reprobados son: {reprobados}")
print(f"Los alumnos aprobados son: {aprobados}")
print(f"Los alumnos excelentes son: {excelentes}")