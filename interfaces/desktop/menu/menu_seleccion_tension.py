

import flet as ft # type: ignore
from typing import TYPE_CHECKING, Type, cast
from enum import Enum

from domain.entities.enums import TensionEnvoltaje
from interfaces.desktop.menu.menu_base import MenuBase


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
    

class MenuSeleccionTension(MenuBase):
    def __init__(self, app: "CalculadoraGARFEX",  enum: Type[Enum], titulo: str) -> None:
        super().__init__(app, enum, titulo)
        
    def ejecutar_opcion(self, opcion: int):
        self.app.page.clean() 
        enum_list: list[TensionEnvoltaje] = cast(list[TensionEnvoltaje], list(self.enum))        
        if opcion and 1 <= int(opcion) <= len(self.enum):
            tension = enum_list[opcion - 1]
            if tension == TensionEnvoltaje.V127:
                self.app.carga.tension = 127
            if tension == TensionEnvoltaje.V220:
                self.app.carga.tension = 220
            if tension == TensionEnvoltaje.V440:
                self.app.carga.tension = 440
            if tension == TensionEnvoltaje.V480:
                self.app.carga.tension = 480
            if tension == TensionEnvoltaje.V13KV:
                self.app.carga.tension = 13200
            if tension == TensionEnvoltaje.V23KV:
                self.app.carga.tension = 23000
            if tension == TensionEnvoltaje.V34KV:
                self.app.carga.tension = 34500
            self.app.menu.get_formulario_potencia()
        elif opcion == int(len(self.enum) + 1): 
            self.app.menu.get_menu_inicio()
        else:
            self.app.page.add(ft.Text("Opción inválida, intenta de nuevo"))