#Gestión de compras:
variable_continuar = True
lista_inicial = ["leche", "pan", "manzanas"]
print("Tu lista de compras actual es: ",lista_inicial)
#Bucle:
while variable_continuar:
    print("-"*60) #separación
    print("Puedes 'agregar', 'eliminar', 'revisar' o 'cerrar' tu lista de compras.")
    accion = input("¿Qué deseas hacer ahora?: ")
    #Condiciones
    if accion.lower() == 'agregar': #.lower() solo puede aplicarse de esta forma y no antes
        producto_agregado = input("Escribe el producto que quieras agregar: ").lower().replace(" ","")
        lista_inicial.append(producto_agregado)
        print("Tu lista de compras actual es: ", lista_inicial)
    elif accion.lower() == 'eliminar':
        producto_eliminado = input("Escribe el producto que quieras eliminar: ").lower().replace(" ","")
        if (producto_eliminado in lista_inicial) == True: #busca el producto en la lista
            lista_inicial.remove(producto_eliminado)
            print("Tu lista de compras actual es: ", lista_inicial)
        else: 
            print("El producto que quieres eliminar no existe en la lista")
    elif accion.lower() == 'revisar':
        print("Tu lista de compras actual es: ",lista_inicial)
    elif accion.lower() == 'cerrar':
        variable_continuar = False
    else: 
        print("La acción introducida es incorrecta.")