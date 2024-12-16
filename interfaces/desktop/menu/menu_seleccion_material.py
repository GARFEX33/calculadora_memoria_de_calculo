

import flet as ft # type: ignore
from typing import TYPE_CHECKING, Type, cast
from enum import Enum

from domain.entities.enums import TipoMaterialCable
from interfaces.desktop.menu.menu_base import MenuBase


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
    

class MenuSeleccionMaterialConductor(MenuBase):
    def __init__(self, app: "CalculadoraGARFEX",  enum: Type[Enum], titulo: str) -> None:
        super().__init__(app, enum, titulo)
        
    def ejecutar_opcion(self, opcion: int):
        self.app.page.clean() 
        enum_list: list[TipoMaterialCable] = cast(list[TipoMaterialCable], list(self.enum))        
        if opcion and 1 <= int(opcion) <= len(self.enum):
            self.app.cable.material   = enum_list[opcion - 1]
            self.app.menu.get_menu_seleccion_canalizacion()
            print(f"Material: {self.app.cable.material}")
        elif opcion == int(len(self.enum) + 1): 
            self.app.menu.get_menu_inicio()
        else:
            self.app.page.add(ft.Text("Opción inválida, intenta de nuevo"))