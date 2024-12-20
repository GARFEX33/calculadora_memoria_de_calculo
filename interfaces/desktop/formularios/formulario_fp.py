from typing import TYPE_CHECKING, Optional
from interfaces.desktop.formularios.formulario_base_numero import FormularioBaseNumero

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class FormularioFP(FormularioBaseNumero):
        def __init__(self, app: "CalculadoraGARFEX", titulo: str, carga: str) -> None:
            super().__init__( app, titulo, carga)

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
          
            if int(str_textfield) < 0 or int(str_textfield) > 100:
                self.mensaje_error.value = f"El campo de {self.carga} debe ser un número entre 0 y 100"
                self.str_textfield.value = ""
                self.app.page.update() # type: ignore
                return


            # Asignar el valor si no está vacío
            self.app.carga.factor_potencia = int(str_textfield)/100
            self.app.page.clean()
            self.app.menu.get_menu_seleccion_carga()

