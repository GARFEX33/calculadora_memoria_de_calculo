from typing import Optional
import flet as ft  # type: ignore
from flet import KeyboardType # type: ignore

class CustomTextField(ft.TextField):
    def __init__(self, label: str, hint_text: str="", multiline: bool=False, keyboard_type:  Optional[KeyboardType]   = None):
        super().__init__(  # type: ignore
            label=label,
            hint_text=hint_text,
            multiline=multiline,
            keyboard_type= keyboard_type,
            text_size=11,
            width = 300,
            height= 45
        )