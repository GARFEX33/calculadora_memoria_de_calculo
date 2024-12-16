import flet as ft # type: ignore
from domain.entities.enums import TipoCarga
from interfaces.desktop.menu.componentes.boton_menu import BotonMenu
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina


class MenuSeleccionCarga:
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
            page.add(ft.Text(f"Has seleccionado: {list(TipoCarga)[int(opcion) - 1].value}"))

        elif opcion == int(len(TipoCarga) + 1):
            from interfaces.desktop.menu.menu_inicial import MenuInicial
            menu_inicial = MenuInicial()
            page.clean()
            menu_inicial.mostrar_menu_inicial(page)
        else:
            page.add(ft.Text("Opción inválida, intenta de nuevo"))
