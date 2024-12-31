import flet as ft # type: ignore
from typing import TYPE_CHECKING
from application.calculadora_service import CalculadoraService
from domain.entities.lista_cables import CableSelecciondo
from interfaces.desktop.memoria_de_calculo.componentes.boton_lista_cables import BotonListaCable
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
        self.app.page.add(TituloPagina("C)  SELECCION DEL CONDUCTOR"))
        self.service.calcular_numero_hilos_carga(self.app)
        self.service.seleccionar_temperatura_cable(self.app)
        self.app.carga.capacidad_conduccion = self.service.seleccion_de_cable_por_capacidad_de_conduccion(self.app)
        self.app.page.add(SubTituloPagina(f"c.1) Por capacidad de conducción: {self.app.carga.capacidad_conduccion:.2f} A"))
        lista_cables = self.service.lista_de_cables_seleccionados(self.app)
        lista = [
            BotonListaCable(cable, metodo_callback= self.seleccionar_cable ,alignment=ft.alignment.center) 
            for cable in lista_cables 
        ]

        self.app.page.add(
            ft.Column(
                controls= lista,
                spacing=1,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        self.app.page.add(ft.OutlinedButton("Volver al menú", on_click= self.volver_menu)) 

    def volver_menu(self,e: ft.ControlEvent):
        self.app.page.clean() 
        self.app.menu.get_menu_inicio()
    
    def seleccionar_cable(self, e: ft.ControlEvent, cable: CableSelecciondo):
        self.app.cable = cable.cable
        self.app.page.clean()
        print("Cable seleccionado", self.app.cable)
        self.app.menu.get_caida_de_tension()