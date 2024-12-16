import flet as ft  # type: ignore
from domain.entities.carga import Carga
from domain.entities.interruptor import Interruptor
from interfaces.desktop.menu.menu_inicial import MenuInicial

class CalculadoraGARFEX:
    def __init__(self) -> None:
        # Inicializa variables que quieras mantener activas durante toda la aplicación
        self.page: ft.Page  
        self.menu_inicial = MenuInicial(self)  
        self.carga = Carga() 
        self.interruptor = Interruptor()  
    
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
        self.menu_inicial.mostrar_menu_inicial( self.page)
    

# Ejecutar la aplicación
if __name__ == "__main__":
    app = CalculadoraGARFEX()  # Crea una instancia de la clase principal
    ft.app(target=app.run) # type: ignore
