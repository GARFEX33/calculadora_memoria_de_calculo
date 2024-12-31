import flet as ft # type: ignore
from typing import Callable, Optional
from flet.core.alignment import Alignment# type: ignore
from domain.entities.lista_cables import CableSelecciondo 

class BotonListaCable(ft.OutlinedButton):
    def __init__(self,  cable: CableSelecciondo,  metodo_callback: Callable[[ft.ControlEvent, CableSelecciondo], None], alignment: Optional[Alignment]  = ft.alignment.center_left)-> None: 
        super().__init__(   # type: ignore
            text= f"SET {cable.cable_por_fase}-{cable.cable.calibre}THHW en {cable.cable.material.value} con {cable.cable.amperaje}A",
            width=400,
            style=ft.ButtonStyle(
                shape= ft.RoundedRectangleBorder(radius=2),  
                 padding=10,
                 alignment= alignment,
            ),  
            on_click=lambda e: metodo_callback(e, cable)
        )