import flet as ft# type: ignore
from interfaces.desktop.menu.componentes.boton_menu import BotonMenu
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina
from interfaces.desktop.menu.menu_seleccion_carga import MenuSeleccionCarga 

class MenuInicial:
    def __init__(self):
        self.__menu_inicial = {
            "1": "Calcular Corriente Nominal y ajustes",
            "2": "Seleccionar Interruptor Termomagnetico",
            "3": "Salir"
        }
        self.__menu_seleccion_carga = MenuSeleccionCarga()

    def mostrar_menu_inicial(self, page: ft.Page):
        # Título del menú
        page.add(TituloPagina("Iniciar Memoria de Calculo"))
        # Crear botones para cada opción
        for key, value in self.__menu_inicial.items():
            page.add(BotonMenu(int(key), value,lambda e, opcion=key: self.ejecutar_opcion(opcion, page), ft.alignment.center))

    def ejecutar_opcion(self, opcion: str, page: ft.Page):
        # Lógica basada en la opción seleccionada
        page.clean()  # Limpia la pantalla para mostrar el contenido de la opción
        if opcion == "1":
            self.__menu_seleccion_carga.mostrar_menu(page)
        elif opcion == "2":
            page.add(ft.Text("Has seleccionado: Seleccionar Interruptor Termomagnetico"))
        elif opcion == "3":
            page.add(ft.Text("¡Gracias por usar la calculadora!"))
            page.update() # type: ignore
            page.window_close()
        else:
            page.add(ft.Text("Opción inválida, intenta de nuevo"))
