import flet as ft # type: ignore
from interfaces.desktop.menu.menu_inicial import MenuInicial  

def main(page: ft.Page):
    page.title = "Calculadora GARFEX"
    page.window.width = 600
    page.window.height = 400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Crear instancia de MenuInicial y mostrarlo
    menu = MenuInicial()
    menu.mostrar_menu_inicial(page)

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main) # type: ignore
