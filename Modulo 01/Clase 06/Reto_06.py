#Inventario de una estación espacial
print("\nBienvenido al inventario espacial...")
#bucle principal
variable_continuar = True
#lista inicial
articulos_espaciales = ["trajes", "alimentos envasados", "botiquin"]
while variable_continuar:
    #menu de opciones
    print("Puedes 'añadir', 'quitar', 'ver', 'inspeccionar' y 'salir' del inventario.")
    menu_opciones = input("¿Qué deseas hacer?: ").lower()
    #Condiciones:
    if menu_opciones == 'añadir':
        articulo_agregado = input("Escribe el artículo que quieras añadir: ").lower().strip()
        if articulo_agregado:
            articulos_espaciales.append(articulo_agregado)
            print("El artículo se agregó con éxito.")
            print(f"El inventario actual es: ", articulos_espaciales)
        else:
            print("Error: No se puede agregar un artículo sin nombre.")
    elif menu_opciones == 'quitar':
        articulo_eliminado = input("Escribe el artículo que quieras quitar: ").lower().strip()
        if (articulo_eliminado in articulos_espaciales) == True:
            articulos_espaciales.remove(articulo_eliminado)
            print("El artículo se eliminó con éxito.")
            print(f"El inventario actual es: ", articulos_espaciales)
        else: 
            print("Error: El artículo que quieres eliminar no existe en el inventario.")
            print(f"El inventario actual es: ", articulos_espaciales)
    elif menu_opciones == 'ver':
        if len(articulos_espaciales) == 0:
            print("El inventario actual está vacío.")
        else:
            print("El inventario actual es: ",sorted(articulos_espaciales)) #orden alfabetico
    elif menu_opciones == 'inspeccionar':
        try:
            item_inspeccionar = int(input("¿Qué item del inventario deseas inspeccionar?: ", ))
            show_item = articulos_espaciales[item_inspeccionar - 1]
            print("El item seleccionado se encontró con éxito.")
            print("El item seleccionado es: ", show_item)
        except ValueError:
            print(f"Error: debes ingresar un número entero entre 1 y {len(articulos_espaciales) + 1}.")
        except Exception as e:
            print(f"Error: Fuera de rango, selecciona un número entre 1 y {len(articulos_espaciales) + 1}.")
    elif menu_opciones == 'salir':
        variable_continuar = False
    else: 
        print("La acción introducida es incorrecta.")