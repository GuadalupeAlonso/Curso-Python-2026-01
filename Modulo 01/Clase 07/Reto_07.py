#Diccionario principal
base_principal = {}
#tupla de materias
materias = ("Resistencia de los materiales", "Control clasico", "Programacion avanzada")
print("\nRegistro de calificaciones de alumnos...")
#Funcion imprimir calificaciones:
def imprimir_calificaciones(diccionario):
    print("  Calificaciones por materia:")
    for materia, calificacion in zip(diccionario["materias inscritas"], diccionario["calificaciones"]): #tuplas de materia: calificacion
        print(f"   {materia}: {calificacion}")
#Comprobar que no se agreguen datos vacios 
def comprobar_dato_vacio(dato):
    if not dato:
        print(f"Error: No puedes introducir un dato vacío.")
        return True #si está vacio
    return False #si no está vacio
#Bucle
while True:
    try:
        print("\nLas acciones disponibles son:\n1. Regitrar alumno \n2. Buscar alumno \n3. Promedio general del alumno \n4. Ver alumnos inscritos \n5. Salir del programa")
        menu = int(input("Introduce el número de la acción que deseas realizar: "))
    except ValueError:
        print("Error: debes ingresar un número entero entre 1 y 5.")
        continue #vuelve al menu principal para obtener un valor correcto 
    
    #Condiciones:
    
    #Registrar
    if menu == 1:
        ID = input("Introduce la matrícula ID del alumno: ").lower()
        #Comprobar que ID no esté vacio
        if comprobar_dato_vacio(ID):
            continue
        #Comprobar que no exista ya
        if ID in base_principal:
            print("El ID introducido ya existe en la lista.")
            continue
        #Ingresar datos alumno 
        nombre = input("Nombre del alumno: ")
        #Comprobar que no esté vacio
        if comprobar_dato_vacio(nombre):
            continue 
        #recibir calificaciones
        print("Materias existentes:\n1. Resistencia de los materiales \n2. Control clasico \n3. Programacion avanzada")
        calificaciones = input("Introduce las calificaciones del alumno en orden a la materia correspondiente con la lista anterior: ")
        lista_calificaciones = calificaciones.split(',')
        #validar que se ingresen unicamente 3 calificaciones  
        if len(lista_calificaciones) != len(materias):
            print("Error: Se deben introducir únicamente tres calificaciones correspondientes a las materias descritas en la lista.")
            continue
        #cambiar formato del dato y comprobar
        errores = [] #lista para indices de calificaciones invalidas
        for i in range(len(lista_calificaciones)):
            try:
                lista_calificaciones[i] = round(float(lista_calificaciones[i].strip()),2) #asignar cambio de formato
            except ValueError:
                errores.append(i) #guarda los items incorrectos
        if errores:
            for i in errores:
                print(f"Error: la calificación '{lista_calificaciones[i]}' no es un número valido. Introduce un número decimal correcto.")
            continue #vuelve al menu y no registra al alumno
        #diccionario para cada alumno y asignar valores si no hubo errores en el registro de calificaciones
        datos_alumno = {
            "nombre": nombre,
            "materias inscritas": materias,
            "calificaciones": lista_calificaciones
        }
        #asignar ID
        base_principal[ID] = datos_alumno #cada alumno se guarda usando su ID como clave, el valor de esa clave es otro diccionario datos_alumno
        #impresion
        print("\nDatos de alumno registrado: ")
        print("  ID del alumno: ", ID.upper())
        print("  Nombre alumno: ", datos_alumno['nombre'].title())
        imprimir_calificaciones(datos_alumno)
    
    #Buscar
    elif menu == 2:
        buscar_ID = input("Introduce la matrícula ID del alumno a buscar: ")
        #Comprobar que ID no esté vacio
        if comprobar_dato_vacio(buscar_ID):
            continue
        #buscar al alumno
        if buscar_ID in base_principal:
            print(f"\nLos datos del alumno con matricula ID {buscar_ID} son: ")
            print("Nombre del alumno: ",base_principal[buscar_ID]['nombre'].title())
            imprimir_calificaciones(base_principal[buscar_ID])
        else:
            print("El ID introducido no se encuentra en la base de datos.")
            continue
    
    #Promedio 
    elif menu == 3:
        buscar_ID = input("Introduce la matrícula ID del alumno a buscar: ")
        #Comprobar que ID no esté vacio
        if comprobar_dato_vacio(buscar_ID):
            continue
        #comprobar que todavia no exista en la lista
        if buscar_ID in base_principal:
            print(f"\nLa lista de calificaciones del alumno {base_principal[buscar_ID]['nombre']} son:")
            imprimir_calificaciones(base_principal[buscar_ID])
            #calcular promedio
            calificaciones_alumno = base_principal[buscar_ID]['calificaciones']
            suma_calificaciones = sum(calificaciones_alumno)
            promedio = suma_calificaciones / len(calificaciones_alumno)
            print("El promedio de sus calificaciones es: ",round(promedio,2))
        else:
            print("El ID introducido no se encuentra en la base de datos.")

    #Ver todos
    elif menu == 4:
        if base_principal:
            print("\nAlumnos inscritos: ")
            for id_alumno, datos in base_principal.items():
                print(f"ID: {id_alumno.upper()} - Nombre: {datos['nombre'].title()}")
        else:
            print("No hay alumnos registrados en la base de datos.")

    #Salir programa
    elif menu == 5:
        break 

    else: 
        print("La acción introducida es incorrecta.")