import flet as ft # type: ignore
from typing import TYPE_CHECKING
from application.calculadora_service import CalculadoraService
from interfaces.desktop.menu.componentes.titulo_pagina import SubTituloPagina, TituloPagina

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX


class MemoriaDeCalculo:
    def __init__(self, app: "CalculadoraGARFEX", service: CalculadoraService) -> None:
        self.app = app
        self.service = service

    def mostrar_memoria(self):
        self.service.calcular_amperaje(self.app.carga)
                # Título del menú
        self.app.page.add(TituloPagina("A)  CALCULO DE LA CORRIENTE NOMINAL"))
        self.app.page.add(SubTituloPagina(f"Corriente nominal: {self.app.carga.corriente_nominal:.2f} A"))
        self.app.page.add(TituloPagina("B)  CALCULO DEL INTERRUPTOR TERMOMAGNETICO"))
        self.service.seleccionar_interruptor( self.app.carga, self.app.interruptor)
        self.app.page.add(SubTituloPagina(f"Interruptor termomagnético seleccionado: {self.service.seleccionar_numero_hilos_interruptor(self.app.carga.tipo_circuito)}X{self.app.interruptor.ampacidad}A"))
        self.app.page.add(ft.OutlinedButton("Volver al menú", on_click= self.volver_menu)) # type: ignore

    def volver_menu(self,e):# type: ignore
        self.app.page.clean() 
        self.app.menu.get_menu_inicio()