from typing import List

def agregar_producto(productos: list):
    """Agrega un producto a la lista."""
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    marca = input("Ingrese la marca del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    productos.append((nombre, precio, marca, cantidad))
    print(f"Producto '{nombre} {marca}' agregado con éxito.")

def mostrar_productos(productos: list):
    """Muestra todos los productos en la lista."""
    if not productos:
        print("No hay productos en la lista.")
        return

    print("\n--- Lista de Productos ---")
    for i, (nombre, precio, marca, cantidad) in enumerate(productos, start=1):
        print(f"{i}. Nombre: {nombre}, Precio: {precio}, Marca: {marca}, Cantidad: {cantidad}")
    print("--------------------------")

def modificar_producto(productos: list):
    """Modifica un producto existente en la lista."""
    if not productos:
        print("No hay productos para modificar.")
        return

    mostrar_productos(productos)

    try:
        indice = int(input("Ingrese el número del producto que desea modificar: ")) - 1
        if indice < 0 or indice >= len(productos):
            print("Índice fuera de rango.")
            return

        nombre, precio, marca, cantidad = productos[indice]
        print("Deje vacío si no desea cambiar un campo.")

        nuevo_nombre = input(f"Nuevo nombre (actual: {nombre}): ") or nombre
        nuevo_precio_input = input(f"Nuevo precio (actual: {precio}): ")
        nuevo_precio = float(nuevo_precio_input) if nuevo_precio_input else precio
        nueva_marca = input(f"Nueva marca (actual: {marca}): ") or marca
        nueva_cantidad_input = input(f"Nueva cantidad (actual: {cantidad}): ")
        nueva_cantidad = int(nueva_cantidad_input) if nueva_cantidad_input else cantidad

        productos[indice] = (nuevo_nombre, nuevo_precio, nueva_marca, nueva_cantidad)
        print("Producto modificado con éxito.")

    except ValueError:
        print("Entrada inválida. Asegúrese de ingresar números donde corresponde.")

def eliminar_producto(productos: list):
    """Elimina un producto de la lista."""
    if not productos:
        print("No hay productos para eliminar.")
        return

    mostrar_productos(productos)

    try:
        indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
        if indice < 0 or indice >= len(productos):
            print("Índice fuera de rango.")
            return

        producto_eliminado = productos.pop(indice)
        print(f"Producto '{producto_eliminado[0]} {producto_eliminado[2]}' eliminado con éxito.")

    except ValueError:
        print("Entrada inválida. Ingrese un número válido.")

def main():
    """Función principal del programa."""
    productos = []

    while True:
        print("\n--- Sistema de Gestión de Productos ---")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(productos)
        elif opcion == "2":
            mostrar_productos(productos)
        elif opcion == "3":
            modificar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
