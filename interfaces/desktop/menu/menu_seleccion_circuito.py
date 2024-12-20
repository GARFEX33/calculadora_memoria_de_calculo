

import flet as ft # type: ignore
from typing import TYPE_CHECKING, Type, cast
from enum import Enum

from domain.entities.enums import TipoCircuito
from interfaces.desktop.menu.menu_base import MenuBase


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
    

class MenuSeleccionCircuito(MenuBase):
    def __init__(self, app: "CalculadoraGARFEX",  enum: Type[Enum], titulo: str) -> None:
        super().__init__(app, enum, titulo)
        
    def ejecutar_opcion(self, opcion: int):
        self.app.page.clean()
        enum_list: list[TipoCircuito] = cast(list[TipoCircuito], list(self.enum))        
        if opcion and 1 <= int(opcion) <= len(self.enum):
            self.app.carga.tipo_circuito = enum_list[opcion - 1]
            self.app.menu.get_menu_seleccion_material_conductor()
        elif opcion == int(len(self.enum) + 1): 
            self.app.menu.get_menu_inicio()
        else:
            self.app.page.add(ft.Text("Opción inválida, intenta de nuevo"))