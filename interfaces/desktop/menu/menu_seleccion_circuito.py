import flet as ft # type: ignore
from typing import TYPE_CHECKING
from domain.entities.enums import TipoCircuito
from interfaces.desktop.menu.componentes.boton_menu import BotonMenu
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX  


class MenuSeleccionCircuito:
    def __init__(self, app:"CalculadoraGARFEX") -> None:
        self.app = app


    def mostrar_menu(self, page: ft.Page):
        page.add(TituloPagina("Seleccione el tipo de Circuito"))
        botones = [
            BotonMenu(idx, carga.value, lambda e, opcion=idx: self.ejecutar_opcion(opcion, page), ft.alignment.center)
            for idx, carga in enumerate(TipoCircuito, start=1)
        ]
        # Botón de salida
        botones.append(
            BotonMenu(len(TipoCircuito) + 1, "Salir", lambda e: self.ejecutar_opcion(len(TipoCircuito) + 1, page), ft.alignment.center)
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
        if opcion and 1 <= int(opcion) <= len(TipoCircuito):
            page.add(ft.Text(f"Has seleccionado: {list(TipoCircuito)[int(opcion) - 1].value}"))

        elif opcion == int(len(TipoCircuito) + 1):
            page.clean()
            self.app.menu_inicial.mostrar_menu_inicial(page)
            
        else:
            page.add(ft.Text("Opción inválida, intenta de nuevo"))
