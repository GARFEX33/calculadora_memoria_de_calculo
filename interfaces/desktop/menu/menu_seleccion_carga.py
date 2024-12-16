import flet as ft # type: ignore
from typing import TYPE_CHECKING

from domain.entities.enums import TipoCarga
from interfaces.desktop.menu.componentes.boton_menu import BotonMenu
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina
from interfaces.desktop.menu.menu_seleccion_circuito import MenuSeleccionCircuito


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
    

class MenuSeleccionCarga:
    def __init__(self, app: "CalculadoraGARFEX") -> None:
        self.app: CalculadoraGARFEX = app
        

    def mostrar_menu(self, page: ft.Page):
        # Título del menú
        page.add(TituloPagina("Seleccione el tipo de Carga"))
        # Crear botones dinámicos para cada opción de TipoCarga
        botones = [
            BotonMenu(idx, carga.value, lambda e, opcion=idx: self.ejecutar_opcion(opcion, page), ft.alignment.center)
            for idx, carga in enumerate(TipoCarga, start=1)
        ]
        # Botón de salida
        botones.append(
            BotonMenu(len(TipoCarga) + 1, "Salir", lambda e: self.ejecutar_opcion(len(TipoCarga) + 1, page), ft.alignment.center)
        )

        # Mostrar botones en un contenedor sin espaciado
        page.add(
            ft.Column(
                controls=botones,
                spacing=1, 
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )    
    def ejecutar_opcion(self, opcion: int, page: ft.Page):
        page.clean()  
        if opcion and 1 <= int(opcion) <= len(TipoCarga):

            menu_circuito = MenuSeleccionCircuito(self.app)
            menu_circuito.mostrar_menu(page)

        elif opcion == int(len(TipoCarga) + 1):
            self.app.menu_inicial.mostrar_menu_inicial(page)
        else:
            page.add(ft.Text("Opción inválida, intenta de nuevo"))
