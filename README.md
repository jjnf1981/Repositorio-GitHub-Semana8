# 🍽️ Sistema de Gestión de Restaurante - Semana 8

**Estudiante:** Joe Jairo Nieto Flores

## 📖 Descripción del sistema

Este proyecto es un sistema de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Permite registrar y listar productos (incluyendo bebidas) y clientes mediante un menú interactivo en consola. Los objetos se crean a partir de datos ingresados por el usuario. El sistema aplica los principios SOLID para mantener un código organizado, extensible y fácil de mantener, destacando la herencia entre `Producto` y `Bebida`, el polimorfismo en el listado y la separación de responsabilidades en clases especializadas.

## 🏗️ Estructura del proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
├── main.py
└── README.md
```

## 📌 Responsabilidad de cada clase

- **Producto**: Representa un producto del restaurante con atributos como código, nombre, categoría y precio. Es la clase base para los productos.
- **Bebida**: Hereda de `Producto` y agrega el atributo específico `tamanio`. Amplía el sistema sin modificar la lógica existente.
- **Cliente**: Representa a un cliente con atributos como identificación, nombre y correo. Se implementa con `@dataclass` para simplificar su definición.
- **Restaurante**: Administra las listas de productos y clientes. Se encarga de agregar y listar elementos, sin interactuar directamente con el usuario.
- **main.py**: Coordina la interacción con el usuario, muestra el menú, solicita datos y llama a los métodos del servicio `Restaurante`.

## 🔗 Relación entre Producto y Bebida

`Bebida` es una clase hija de `Producto`. Esto significa que una bebida **es un tipo de producto**. La clase `Bebida` hereda todos los atributos y métodos de `Producto` y añade su propio atributo específico (`tamanio`). Esta relación permite que tanto `Producto` como `Bebida` se almacenen en la misma lista y se traten de forma polimórfica, sin que el servicio necesite distinguir entre ellos.

## 🧩 Principios SOLID aplicados

- **Responsabilidad Única (SRP)**:
  - `Producto` y `Bebida` solo representan productos.
  - `Cliente` solo representa un cliente.
  - `Restaurante` solo administra colecciones.
  - `main.py` solo maneja la interacción por consola.

- **Abierto/Cerrado (OCP)**:
  El sistema está abierto para la extensión (se agregó `Bebida` sin modificar `Producto` ni `Restaurante`) y cerrado para la modificación de la lógica existente.

- **Sustitución de Liskov (LSP)**:
  `Bebida` puede ser utilizada en cualquier lugar donde se espere un objeto de tipo `Producto`, sin alterar el comportamiento del programa. Esto se demuestra al almacenar y listar `Producto` y `Bebida` en la misma colección sin necesidad de condicionales.

## 💻 Instrucciones de ejecución

1. Asegúrate de tener Python 3.x instalado.
2. Clona o descarga el repositorio.
3. Ubícate en la carpeta `restaurante_app`.
4. Ejecuta el programa con el comando:

```bash
python main.py
```

## 🤔 Reflexión personal

Diseñar un proyecto mantenible ha sido clave para entender cómo estructurar el código de forma clara y profesional. Aplicar los principios SOLID, especialmente la herencia y el polimorfismo, me ha permitido agregar nuevas funcionalidades (como la clase `Bebida`) sin modificar el código existente, reduciendo el riesgo de errores. Separar las responsabilidades en clases específicas ha facilitado la organización y la comprensión del sistema. Este enfoque no solo hace que el código sea más fácil de extender y depurar, sino que también prepara el proyecto para futuros cambios y colaboraciones en equipo. Aprender a diseñar pensando en la mantenibilidad es una habilidad esencial para cualquier desarrollador.