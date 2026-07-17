# ==========================================================
# CLASE: Bebida, hija de Producto
# ==========================================================

from modelos.producto import Producto

class Bebida(Producto):
    """
    Representa una bebida registrada en el restaurante.

    Principio OCP:
    El sistema se amplía agregando esta nueva clase sin modificar
    el funcionamiento de Producto ni la lógica de listado.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamanio: str,
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)

        self._tamanio = tamanio

    @property
    def tamanio(self) -> str:
        """Devuelve el tamaño de la bebida."""
        return self._tamanio

    def mostrar_informacion(self) -> str:
        """
        Devuelve la información específica de una bebida.

        Este método sobrescribe el comportamiento definido
        en Producto.
        """
        return (
            f"Código: {self.codigo} | "
            f"Bebida: {self.nombre} | "            
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamanio}"
        )