import flet as ft  # type: ignore
from typing import TYPE_CHECKING, Optional
from flet import KeyboardType  # type: ignore

from interfaces.desktop.formularios.componentes.custom_textfield import CustomTextField
from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class FormularioBaseNumero:
    def __init__(self, app: "CalculadoraGARFEX", titulo: str, carga: str):
        self.app = app
        self.str_textfield = CustomTextField(carga, f"Ingresa {carga}", keyboard_type=KeyboardType.NUMBER) 
        self.enviar_textfield = ft.ElevatedButton(text="Enviar", on_click=self.enviar_click) # type: ignore
        self.mensaje_error = ft.Text("", color="red")  # Único mensaje de error dinámico
        self.titulo = titulo
        self.carga = carga
    
    def enviar_click(self, e) -> None:  # type: ignore
        str_textfield: Optional[str] = (
            self.str_textfield.value.strip()
            if self.str_textfield.value
            else None
        )
        # Limpiar mensaje de error
        self.mensaje_error.value = ""

        # Validar que el campo no esté vacío
        if not str_textfield:
            self.mensaje_error.value = f"El campo de {self.carga} no puede estar vacío"
            self.str_textfield.value = ""
            self.app.page.update()  # type: ignore
            return  # Detener la ejecución si el campo está vacío
        if not str_textfield.isdigit():
            self.mensaje_error.value = f"El campo de {self.carga} debe ser un número"
            self.str_textfield.value = ""
            self.app.page.update() # type: ignore
            return # Detener la ejec

        # Asignar el valor si no está vacío
        self.app.carga.potencia = int(str_textfield)
        self.app.page.clean()
        self.app.menu.get_formulario_fp()

    def mostrar_formulario_carga(self):
        self.app.page.add(TituloPagina(self.titulo))
        formulario = [
            self.str_textfield,
        ]
        self.app.page.add(
            ft.Column(
                controls=formulario,  # type: ignore
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        self.app.page.add(
            ft.Row(
                controls=[
                    self.enviar_textfield,
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )
        self.app.page.add(self.mensaje_error)  # Mostrar mensaje dinámico
