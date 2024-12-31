import flet as ft # type: ignore
from flet.core.alignment import Alignment # type: ignore
from typing import Callable, Optional

class BotonMenu(ft.OutlinedButton):
    def __init__(self, idx: int, menu: str, metodo_callback: Callable[[int], None], alignment: Optional[Alignment]  = ft.alignment.center_left )-> None: 
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