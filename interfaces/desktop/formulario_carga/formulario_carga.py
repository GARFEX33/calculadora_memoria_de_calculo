
from typing import TYPE_CHECKING

from interfaces.desktop.menu.componentes.titulo_pagina import TituloPagina


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
class FormularioCarga:
    def __init__(self, app: "CalculadoraGARFEX" ):
        self.app = app
        self.input_nombre = "nombre"
    
    def mostrar_formulario_carga(self):
        self.app.page.add(TituloPagina("Formulario de carga"))
