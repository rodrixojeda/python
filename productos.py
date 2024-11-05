import os

# Lista que contendrá los productos
productos = []

# Función para cargar los datos desde un archivo
def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })

# Función para guardar los datos en un archivo
def guardar_datos():
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados exitosamente.")

# Función para añadir un producto
def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            cantidad = int(input("Introduce la cantidad del producto: "))
            break
        except ValueError:
            print("Error: Por favor, introduce valores válidos para el precio y la cantidad.")
    
    productos.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print(f"Producto '{nombre}' añadido correctamente.")

# Función para ver todos los productos
def ver_productos():
    if productos:
        print("\nLista de productos:")
        for idx, producto in enumerate(productos, 1):
            print(f"{idx}. Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario.")

# Función para actualizar un producto
def actualizar_producto():
    ver_productos()
    if productos:
        nombre = input("\nIntroduce el nombre del producto a actualizar: ")
        for producto in productos:
            if producto["nombre"] == nombre:
                print(f"Producto seleccionado: {producto}")
                nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para no cambiar): ") or producto["nombre"]
                while True:
                    try:
                        nuevo_precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
                        nuevo_precio = float(nuevo_precio) if nuevo_precio else producto["precio"]
                        nueva_cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")
                        nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto["cantidad"]
                        break
                    except ValueError:
                        print("Error: Por favor, introduce valores válidos para el precio y la cantidad.")
                
                producto["nombre"] = nuevo_nombre
                producto["precio"] = nuevo_precio
                producto["cantidad"] = nueva_cantidad
                print(f"Producto '{nombre}' actualizado correctamente.")
                return
        print(f"Producto con nombre '{nombre}' no encontrado.")

# Función para eliminar un producto
def eliminar_producto():
    ver_productos()
    if productos:
        nombre = input("\nIntroduce el nombre del producto a eliminar: ")
        for producto in productos:
            if producto["nombre"] == nombre:
                productos.remove(producto)
                print(f"Producto '{nombre}' eliminado correctamente.")
                return
        print(f"Producto con nombre '{nombre}' no encontrado.")

# Función del menú principal
def menu():
    cargar_datos()  # Cargar los datos al iniciar
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")
menu()