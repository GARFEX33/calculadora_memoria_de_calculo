from typing import TYPE_CHECKING
from domain.entities.enums import *
from interfaces.desktop.formulario_carga.formulario_carga import FormularioCarga
from interfaces.desktop.menu.menu_inicial import MenuInicial
from interfaces.desktop.menu.menu_seleccion_canalizacion import MenuSeleccionCanalizacion
from interfaces.desktop.menu.menu_seleccion_carga import MenuSeleccionCarga
from interfaces.desktop.menu.menu_seleccion_circuito import MenuSeleccionCircuito
from interfaces.desktop.menu.menu_seleccion_material import MenuSeleccionMaterialConductor


if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class MenuService:
    def __init__(self, app: "CalculadoraGARFEX" ) -> None:
        self.app = app
    def get_menu_inicio(self):
        return MenuInicial(self.app).mostrar_menu_inicial()
    
    def get_menu_seleccion_carga(self):
        return MenuSeleccionCarga(self.app, TipoCarga, "Selecciona carga").mostrar_menu( )
    
    def get_menu_seleccion_circuito(self):
        return MenuSeleccionCircuito(self.app, TipoCircuito, "Selecciona circuito").mostrar_menu()
    
    def get_menu_seleccion_material_conductor(self):
        return MenuSeleccionMaterialConductor(self.app, TipoMaterialCable, "Selecciona material de conductor").mostrar_menu()
    
    def get_menu_seleccion_canalizacion(self):
        return MenuSeleccionCanalizacion(self.app, Canalizacion , "Selecciona canalizacion").mostrar_menu()
    
    def get_formulario_carga(self):
        return FormularioCarga(self.app).mostrar_formulario_carga()