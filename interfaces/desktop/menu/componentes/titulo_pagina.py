import flet as ft  # type: ignore

class TituloPagina(ft.Text):
    def __init__(self, titulo: str):
        super().__init__(  # type: ignore
            value=titulo,
            size=18,
            weight=ft.FontWeight.BOLD
        )
class SubTituloPagina(ft.Text):
    def __init__(self, titulo: str):
        super().__init__(  # type: ignore
            value=titulo,
            size=16,
            weight=ft.FontWeight.BOLD
        )
