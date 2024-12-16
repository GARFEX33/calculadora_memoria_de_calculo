import flet as ft # type: ignore
from typing import Callable

class BotonMenu(ft.OutlinedButton):
    def __init__(self, idx: int, menu: str, metodo_callback: Callable[[int], None], alignment  = ft.alignment.center_left )-> None: # type: ignore
        super().__init__(  # type: ignore
            text= f"{menu}",
            width=300,
            style=ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=2),  
                 padding=10,
                 alignment= alignment,
            ),  
            on_click=lambda e: metodo_callback(idx)
        )