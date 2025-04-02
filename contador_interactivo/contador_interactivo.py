"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """
    Representa el estado de la aplicación.

    Atributos:
        contador (int): Un contador que almacena un valor numérico que puede ser incrementado o decrementado
    """
    contador:int = 0

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

    ...

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
                color_scheme = "green",
                on_click = State.incrementar
                ),
                rx.heading(
                State.contador,
                font_size = "2em"
                ),
                rx.button(
                "Decrementar",
                color_scheme = "red",
                on_click = State.decrementar              
                ),
                spacing="5",
                justify="center",
                min_height="85vh",
            ),
        )
    )

app = rx.App()
app.add_page(index)
