import flet as ft # type: ignore
from typing import TYPE_CHECKING

from interfaces.desktop.menu.componentes.boton_menu import BotonMenu
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina
if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class MenuInicial:
    def __init__(self, app: "CalculadoraGARFEX") -> None:
            self.__menu_inicial = {
                "1": "Calcular Corriente Nominal y ajustes",
                "2": "Seleccionar Interruptor Termomagnetico",
                "3": "Salir"
            }
            self.app: CalculadoraGARFEX = app
        
        
    def mostrar_menu_inicial(self):
        self.app.page.add(TituloPagina("Iniciar Memoria de Calculo"))
        for key, value in self.__menu_inicial.items():
            self.app.page.add(BotonMenu(int(key), value,lambda e, opcion=key: self.ejecutar_opcion(opcion), ft.alignment.center))

    def ejecutar_opcion(self, opcion: str):
        self.app.page.clean()  
        if opcion == "1":
            self.app.opcion = opcion
            self.app.menu.get_formulario_nombre_carga()
        elif opcion == "2":
            self.app.opcion = opcion
            self.app.page.add(ft.Text("Has seleccionado: Seleccionar Interruptor Termomagnetico"))
        elif opcion == "3":
            self.app.page.add(ft.Text("¡Gracias por usar la calculadora!"))
            self.app.page.update() # type: ignore
            self.app.page.window_close()
        else:
            self.app.page.add(ft.Text("Opción inválida, intenta de nuevo"))
