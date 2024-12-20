from typing import TYPE_CHECKING
from interfaces.desktop.formularios.formulario_base_numero import FormularioBaseNumero

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class FormularioPotencia(FormularioBaseNumero):
        def __init__(self, app: "CalculadoraGARFEX", titulo: str, carga: str) -> None:
            super().__init__( app, titulo, carga)

