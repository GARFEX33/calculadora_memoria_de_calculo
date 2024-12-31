import flet as ft # type: ignore
from flet.core.control import Control # type: ignore

from typing import TYPE_CHECKING, Optional, Sequence
from application.calculadora_service import CalculadoraService
from interfaces.desktop.formularios.componentes.custom_textfield import CustomTextField
from interfaces.desktop.menu.componentes.titulo_pagina import  TituloPagina

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX


class CaidaDeTensionCalculo:
    def __init__(self, app: "CalculadoraGARFEX", service: CalculadoraService) -> None:
        self.app = app
        self.service = service
        self.str_textfield = CustomTextField("Longitud", "Ingresa la longitud del cable", keyboard_type=ft.KeyboardType.NUMBER)
        self.enviar_textfield = ft.ElevatedButton(text="Calcular Caida", on_click=self.calcular_caida) 
        self.mensaje_error = ft.Text("", color="red")  
        self.str_caida_de_tension = ft.Text("") 


    def mostrar_caida_de_tension(self):
        self.service.calcular_amperaje(self.app.carga)
        self.app.page.add(TituloPagina("D) CAIDA DE TENSION REAL"))
        contenido: Optional[Sequence[Control]]  = [
            ft.Text(f"Calibre seleccionado: {self.app.cable.calibre} " ),
           self.str_textfield,
              self.enviar_textfield,
                self.mensaje_error,
                self.str_caida_de_tension,
        ]   
        self.app.page.add(
            ft.Column(
                controls= contenido,
                spacing=1,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

        self.app.page.add(ft.OutlinedButton("Volver al menú", on_click= self.volver_menu)) 

    def volver_menu(self,e: ft.ControlEvent):
        self.app.page.clean() 
        self.app.menu.get_menu_inicio()
    
    def calcular_caida(self, e: ft.ControlEvent):
        str_textfield: Optional[str] = (
            self.str_textfield.value.strip()
            if self.str_textfield.value
            else None
              )
                # Limpiar mensaje de error
        self.mensaje_error.value = ""
        # Validar que el campo no esté vacío
        if not str_textfield:
            self.mensaje_error.value = f"El campo de no puede estar vacío"
            self.str_textfield.value = ""
            self.app.page.update()  # type: ignore
            return  # Detener la ejecución si el campo está vacío        
        if not str_textfield.isdigit():
            self.mensaje_error.value = f"El campo debe ser un número"
            self.str_textfield.value = ""
            self.app.page.update() # type: ignore
            return # Detener la ejec
        
        
        self.app.carga.longitud = int(str_textfield)

        self.service.seleccionar_seccion_cable(self.app.cable)
        self.service.calcular_caida_de_tension(self.app)
        
        self.str_caida_de_tension.value = f"Caida de tensión: {self.app.carga.caida_tension:.2f}%"
        print(self.app.cable)
        self.app.page.update() # type: ignore
