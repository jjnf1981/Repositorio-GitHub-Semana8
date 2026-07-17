# ==========================================================
# CLASE: Restaurante
# ==========================================================

from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    """
    Servicio encargado de administrar productos y clientes.

    Principio SRP:
    Su responsabilidad es gestionar las colecciones del restaurante.

    Esta clase no solicita datos mediante input() y tampoco muestra
    el menú de la aplicación. Esa responsabilidad pertenece a main.py.
    """
        
    # Administra los productos y clientes del restaurante.
    def __init__(self) -> None:
        self.productos: list[Producto] = [] # Almacena la lista de productos o de sus subclases.
        self.clientes = [] # Almacena la lista de clientes del restaurante.

    # Métodos para gestionar productos
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un producto (o bebida) a la lista.
        La anotación Producto permite recibir objetos
        Producto o cualquier futura clase hija válida.
        """
        
        self.productos.append(producto)

    # Métodos para gestionar clientes
    def agregar_cliente(self, cliente: Cliente) -> None:
        # Agrega un cliente a la lista de clientes del restaurante.
        self.clientes.append(cliente)

    def listar_productos(self) -> list[Producto]:
        """
        Devuelve la información de todos los productos.

        Polimorfismo:
        Cada objeto responde al mismo método mostrar_informacion(),
        pero Producto y Bebida generan información diferente.
        """
                
        return self.productos

    def listar_clientes(self) -> list[Cliente]:
        # Retorna la lista de clientes del restaurante.
        return self.clientes