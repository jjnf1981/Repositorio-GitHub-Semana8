# ==========================================================
# ARCHIVO PRINCIPAL (main.py)
# ==========================================================

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante
from modelos.bebida import Bebida

def mostrar_menu() -> None:
    """
    Muestra el menú principal del sistema.

    Esta función solamente muestra el menú.
    No registra ni modifica directamente las colecciones.
    """
        
    print("\n" + "=" * 40)
    print("         SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")
    print("=" * 40)

# Metodo para registrar un productos
def registrar_producto(restaurante) -> None:
    #Función para registrar productos en el restaurante.
    print("\n--- Registrar producto ---")
    
    while True:
        codigo = str(input("\nIngrese el código del producto: "))
        if codigo.strip:
            break  # Sale del bucle porque el código es válido
        print("El código no puede estar vacío. Intente nuevamente.")

    while True:
        nombre = input("\nIngrese el nombre del producto: ")
        if nombre.strip():
            break  # Sale del bucle porque el nombre es válido
        print("El nombre no puede estar vacío. Intente nuevamente.")

    while True:
        categoria = input("\nIngrese la categoría del producto: ")
        if categoria.strip():
            break  # Sale del bucle porque la categoría es válida
        print("La categoría no puede estar vacía. Intente nuevamente.")
        
    while True:
        try:
            precio = float(input("\nIngrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero. Intente nuevamente.")
                continue  # Vuelve a pedir el precio
            break  # Sale del bucle porque el precio es correcto
        except ValueError:
            print("Error, ingrese un número válido para el precio.")
    
    producto = Producto(codigo, nombre, categoria, precio)
    restaurante.agregar_producto(producto)
    print(f"\nEl Producto '{nombre}' se registró exitosamente.")

# Metodo para registrar bebidas
def registrar_bebida(restaurante) -> None:
    #Función para registrar bebidas en el restaurante.
    print("\n--- Registrar bebida ---")

    while True:
        codigo = str(input("\nIngrese el código del producto: "))
        if codigo.strip:
            break  # Sale del bucle porque el código es válido
        print("El código no puede estar vacío. Intente nuevamente.")

    while True:
        nombre = input("\nIngrese el nombre de la bebida: ")
        if nombre.strip():
            break  # Sale del bucle porque el nombre es válido
        print("El nombre no puede estar vacío. Intente nuevamente.")

    while True:
        categoria = input("\nIngrese la categoría de la bebida: ")
        if categoria.strip():
            break  # Sale del bucle porque la categoría es válida
        print("La categoría no puede estar vacía. Intente nuevamente.")

    while True:
        try:
            precio = float(input("\nIngrese el precio de la bebida: "))
            if precio <= 0:
                print("El precio debe ser mayor que cero. Intente nuevamente.")
                continue  # Vuelve a pedir el precio
            break  # Sale del bucle porque el precio es correcto
        except ValueError:
            print("Error, ingrese un número válido para el precio.")

    while True:
        tamanio = input("\nIngrese el tamaño de la bebida: ")
        if tamanio.strip():
            break  # Sale del bucle porque el tamaño es válido
        print("El tamaño no puede estar vacío. Intente nuevamente.")

    bebida = Bebida(codigo, nombre, categoria, precio, tamanio)
    restaurante.agregar_producto(bebida)
    print(f"\nLa Bebida '{nombre}' se registró exitosamente.")

# Metodo para registrar un cliente
def registrar_cliente(restaurante) -> None:
    #Función para registrar clientes en el restaurante.
    print("\n--- Registrar cliente ---")

    while True:
        identificacion = str(input("\nIngrese la identificación del cliente: "))
        if identificacion.strip():
            break  # Sale del bucle porque la identificación es válida
        print("La identificación no puede estar vacía. Intente nuevamente.")

    while True:
        nombre = input("\nIngrese el nombre del cliente: ")
        if nombre.strip():
            break  # Sale del bucle porque el nombre es válido
        print("El nombre no puede estar vacío. Intente nuevamente.")

    while True:
        correo = input("\nIngrese el email del cliente: ")
        if correo.strip():
            break  # Sale del bucle porque el email es válido
        print("El email no puede estar vacío. Intente nuevamente.")

    cliente = Cliente(identificacion, nombre, correo)
    restaurante.agregar_cliente(cliente)
    print(f"\nEl cliente '{nombre}' se registró exitosamente.")

# Metodo para listar productos
def listar_productos(restaurante) -> None:
    #Función para mostrar todos los productos registrados.
    print("\n--- Lista de productos ---")
    productos = restaurante.listar_productos()  # Guardamos la lista una sola vez
    if not productos:
        print("\nNo existen productos registrados.")
        return
    
    for producto in productos:
        print(producto.mostrar_informacion())

# Metodo para listar clientes
def listar_clientes(restaurante) -> None:
    #Función para mostrar todos los clientes registrados.
    print("\n--- Lista de clientes ---")
    clientes = restaurante.listar_clientes()  # Guardamos la lista una sola vez
    if not clientes:
        print("\nNo existen clientes registrados.")
        return

    for cliente in clientes:
        print(cliente.mostrar_informacion())

def main():

    restaurante = Restaurante()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            registrar_bebida(restaurante)
        elif opcion == "3":
            registrar_cliente(restaurante)
        elif opcion == "4":
            listar_productos(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            print("\nGracias por utilizar el sistema Restaurante.\n")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

# Punto de inicio del programa
if __name__ == "__main__":
    main()