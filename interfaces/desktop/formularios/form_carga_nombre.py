
from typing import TYPE_CHECKING
from interfaces.desktop.formularios.formulario_base_string import FormularioBaseString
if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class FormularioCarga(FormularioBaseString):
        def __init__(self, app: "CalculadoraGARFEX", titulo: str, carga: str) -> None:
            super().__init__( app, titulo, carga)

