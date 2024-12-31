from abc import ABC, abstractmethod
import flet as ft # type: ignore
from enum import Enum

from typing import TYPE_CHECKING, Type

from interfaces.desktop.menu.componentes.boton_menu import BotonMenu
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina
if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

    

class MenuBase(ABC):
    def __init__(self, app: "CalculadoraGARFEX", enum: Type[Enum], titulo:str ) -> None:
        self.app = app
        self.enum = enum
        self.titulo = titulo
    
    def mostrar_menu(self):
        # Título del menú
        self.app.page.add(TituloPagina(self.titulo))
        # Crear botones dinámicos para cada opción de TipoCarga
        botones = [
            BotonMenu(idx, carga.value, lambda e, opcion=idx: self.ejecutar_opcion(opcion), ft.alignment.center)
            for idx, carga in enumerate(self.enum, start=1) # type: ignore
        ]
        # Botón de salida
        botones.append(
            BotonMenu(len(self.enum) + 1, "Salir", lambda e: self.ejecutar_opcion(len(self.enum) + 1), ft.alignment.center) 
        )

        # Mostrar botones en un contenedor sin espaciado
        self.app.page.add(
            ft.Column(
                controls=botones,
                spacing=1, 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )    
    @abstractmethod
    def ejecutar_opcion(self, opcion: int) -> None:
        pass

