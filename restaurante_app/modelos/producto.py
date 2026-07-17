# ==========================================================
# CLASE: Producto, aplicando encapsulación con @property y @setter
# ==========================================================

class Producto:
    """
    Representa un producto del restaurante.
    Es la clase base para productos y bebidas.
    """
        
    # Uso de Constructor tradicional.
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float):
        self.codigo = codigo # Almacena el código del producto.
        self.nombre = nombre # Almacena el nombre del producto.
        self.categoria = categoria # Almacena la categoría del producto.
        self.precio = precio # Almacena el precio del producto.

    # Propiedad y setter para código
    @property
    def codigo(self) -> str:
        # Devuelve el código del producto.
        return self._codigo

    @codigo.setter
    def codigo(self, nuevo_codigo: str):
        """Setter: asigna el código con validación (no vacío)."""
        if not nuevo_codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        self._codigo = nuevo_codigo

    # Propiedad y setter para nombre
    @property
    def nombre(self) -> str:
        # Devuelve el nombre del producto.
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        """Setter: asigna el nombre con validación (no vacío)."""
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    # Propiedad y setter para categoría
    @property
    def categoria(self) -> str:
        # Devuelve la categoría del producto.
        return self._categoria

    @categoria.setter
    def categoria(self, nueva_categoria: str):
        # Permite actualizar la categoría del producto.
        if not nueva_categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        self._categoria = nueva_categoria

    # Propiedad y setter para precio
    @property
    def precio(self) -> float:
        # Devuelve el valor del producto.
        return self._precio
    
    @precio.setter
    def precio(self, nuevo_precio: float):
        # Permite actualizar el valor del producto.
        if nuevo_precio <= 0:
            raise ValueError("El precio no puede ser cero o negativo.")
        self._precio = nuevo_precio

    # Método para mostrar información del producto
    def mostrar_informacion(self) -> str:
        # Retorna una cadena de texto con la información principal del producto.
        return (
            f"Código: {self.codigo} | "
            f"Producto: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f}"
        )