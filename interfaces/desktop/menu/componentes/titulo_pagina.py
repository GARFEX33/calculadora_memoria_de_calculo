import flet as ft  # type: ignore

class TituloPagina(ft.Text):
    def __init__(self, titulo: str):
        super().__init__(  # type: ignore
            value=titulo,
            size=20,
            weight=ft.FontWeight.BOLD
        )