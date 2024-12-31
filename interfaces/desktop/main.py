import flet as ft  # type: ignore
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion
from domain.entities.interruptor import Interruptor
from interfaces.desktop.servicios.menu_service import MenuService


class CalculadoraGARFEX:
    def __init__(self) -> None:
        # Inicializa variables que quieras mantener activas durante toda la aplicación
        self.page: ft.Page  
        self.menu: MenuService = MenuService(self)
        self.carga = Carga()
        self.cable = Cable()
        self.interruptor = Interruptor()
        self.canalizacion: Canalizacion = Canalizacion.TUBERIA
        self.opcion: str = ""   
    
    def run(self, page: ft.Page) -> None:
        """
        Método principal para ejecutar la aplicación.
        """
        # Configuración de la página principal
        self.page = page
        self.page.title = "Calculadora GARFEX"
        self.page.window.width  = 600
        self.page.window.height = 400
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.START

        # Mostrar el menú inicial
        self.menu.get_menu_inicio()
    

# Ejecutar la aplicación
if __name__ == "__main__":
    app = CalculadoraGARFEX()  # Crea una instancia de la clase principal
    ft.app(target=app.run) # type: ignore
