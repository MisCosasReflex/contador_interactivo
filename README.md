
# Contador Interactivo con Reflex

Esta aplicación es un ejemplo básico creado utilizando el framework [Reflex](https://reflex.dev/). Proporciona un contador interactivo que permite al usuario incrementar y decrementar el valor del contador en tiempo real. La arquitectura de la aplicación separa la lógica y el manejo del estado (en la clase `State`) de la definición de la interfaz de usuario (en la función `index()`), lo que facilita el mantenimiento y la escalabilidad.

## Características

- **Estado Reactivo:**  
  La clase `State` extiende `rx.State` y centraliza la lógica de la aplicación. Cualquier cambio en las variables de estado se refleja automáticamente en la interfaz de usuario.
  
- **Interfaz de Usuario Sencilla:**  
  La función `index()` define la vista principal utilizando componentes predefinidos de Reflex, como contenedores, botones, y textos.

- **Actualización en Tiempo Real:**  
  Gracias a la reactividad de Reflex, la UI se actualiza inmediatamente cuando se realizan acciones (como hacer clic en un botón), sin la necesidad de recargar la página.

## Estructura del Proyecto

El proyecto consta de los siguientes elementos principales:

- **State:**  
  Clase que contiene la lógica y el estado de la aplicación. Se definen métodos para incrementar y decrementar el contador.

- **index():**  
  Función que construye y retorna el componente principal de la aplicación, integrando los elementos visuales y enlazándolos con los controladores de eventos del `State`.

- **app:**  
  Instancia de `rx.App()` que configura y arranca el servidor web integrado de Reflex, y que asigna la función `index()` a la ruta principal.

## Requisitos

- Python 3.7 o superior.
- [Reflex](https://reflex.dev/) instalado en el entorno de desarrollo.
- Dependencias adicionales según `rxconfig` (configuración propia de tu entorno).

## Instalación y Ejecución

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/MisCosasReflex/contador_interactivo.git
   ```
2. **Navega al directorio del proyecto:**
   ```bash
   cd contador_interactivo
   ```
3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecuta la aplicación:**
   ```bash
   reflex init
   reflex run
   ```
   Al iniciar, el servidor web de Reflex se ejecutará y la aplicación estará disponible (por defecto en `http://localhost:8000`).

## Ejemplo de Código

El siguiente fragmento de código muestra la estructura completa de este proyecto de ejemplo:

```python
"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from rxconfig import config


class State(rx.State):
    """
    Representa el estado de la aplicación.

    Atributos:
        contador (int): Un contador reactivo para gestionar el valor numérico.
    """
    contador: int = 0

    def incrementar(self) -> None:
        """
        Incrementa el valor del contador en 1.

        Este método se utiliza como manejador de eventos para actualizar el estado interno 
        cuando se requiere aumentar el valor del contador.
        """
        self.contador += 1

    def decrementar(self) -> None:
        """
        Decrementa el valor del contador en 1.

        Este método se utiliza como manejador de eventos para actualizar el estado interno 
        cuando se requiere disminuir el valor del contador.
        """
        self.contador -= 1


def index() -> rx.Component:
    """
    Construye y retorna el componente principal de la página de bienvenida de la aplicación.

    La función index crea un contenedor que agrupa varios componentes de la interfaz:
      - Un botón para cambiar el modo de color, ubicado en la parte superior derecha.
      - Un centro que contiene un conjunto vertical de elementos:
          • Un encabezado con el título "Contador Interactivo".
          • Un texto descriptivo que instruye al usuario para incrementar o decrementar el contador.
          • Un botón "Incrementar" que, al hacer clic, ejecuta el método State.incrementar.
          • Un encabezado que muestra el valor actual del contador.
          • Un botón "Decrementar" que, al hacer clic, ejecuta el método State.decrementar.
    
    Returns:
        rx.Component: El componente que representa la vista principal de la aplicación.
    """
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.center(
            rx.vstack(
                rx.heading("Contador Interactivo", size="9"),
                rx.text(
                    "Incremente o decremente el valor haciendo clic en los respectivos botones",
                    size="5",
                    justify="center",
                ),
                rx.button(
                    "Incrementar",
                    color_scheme="green",
                    on_click=State.incrementar,
                ),
                rx.heading(
                    State.contador,
                    font_size="2em",
                ),
                rx.button(
                    "Decrementar",
                    color_scheme="red",
                    on_click=State.decrementar,
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        )
    )


app = rx.App()
app.add_page(index)

if __name__ == "__main__":
    app.run()
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar esta aplicación, por favor abre un *issue* o envía un *pull request* para sugerir cambios o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más información.