# ==========================================================
# CLASE: Cliente, usando @dataclass
# ==========================================================

from dataclasses import dataclass

@dataclass
class Cliente:
    """
    Representa un cliente registrado en el restaurante.

    Principio SRP:
    Esta clase solamente administra la información propia de un cliente.
    No registra productos ni controla el menú del programa.
    """
    
    # El @dataclass generar automáticamente el constructor.
    identificacion: int
    nombre: str
    correo: str

    def mostrar_informacion(self) -> str:
        # Retorna una cadena de texto con la información del cliente.
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )