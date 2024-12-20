

import flet as ft # type: ignore
from typing import TYPE_CHECKING, Type, cast
from enum import Enum

from domain.entities.enums import Canalizacion
from interfaces.desktop.menu.menu_base import MenuBase


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
    

class MenuSeleccionCanalizacion(MenuBase):
    def __init__(self, app: "CalculadoraGARFEX",  enum: Type[Enum], titulo: str) -> None:
        super().__init__(app, enum, titulo)
        
    def ejecutar_opcion(self, opcion: int):
        self.app.page.clean() 
        enum_list: list[Canalizacion] = cast(list[Canalizacion], list(self.enum))        
        if opcion and 1 <= int(opcion) <= len(self.enum):
            self.app.canalizacion = enum_list[opcion - 1] 
            self.app.menu.get_memoria_de_calculo()
        elif opcion == int(len(self.enum) + 1): 
            self.app.menu.get_menu_inicio()
        else:
            self.app.page.add(ft.Text("Opción inválida, intenta de nuevo"))