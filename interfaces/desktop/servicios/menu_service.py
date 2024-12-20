from typing import TYPE_CHECKING
from application.calculadora_service import CalculadoraService
from domain.entities.enums import *
from interfaces.desktop.formularios.form_carga_nombre import FormularioCarga
from interfaces.desktop.formularios.formulario_fp import FormularioFP
from interfaces.desktop.formularios.formulario_potencia import FormularioPotencia
from interfaces.desktop.memoria_de_calculo.calculo_corriente_nominal import MemoriaDeCalculo
from interfaces.desktop.menu.menu_inicial import MenuInicial
from interfaces.desktop.menu.menu_seleccion_canalizacion import MenuSeleccionCanalizacion
from interfaces.desktop.menu.menu_seleccion_carga import MenuSeleccionCarga
from interfaces.desktop.menu.menu_seleccion_circuito import MenuSeleccionCircuito
from interfaces.desktop.menu.menu_seleccion_material import MenuSeleccionMaterialConductor
from interfaces.desktop.menu.menu_seleccion_tension import MenuSeleccionTension

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
    
    def get_formulario_nombre_carga(self):
        return  FormularioCarga(self.app, "Ingresa Nombre de Carga", "Carga").mostrar_formulario_carga()

    def get_menu_seleccion_tension(self):
        return MenuSeleccionTension(self.app, TensionEnvoltaje, "Selecciona tensión").mostrar_menu()
   
    def get_formulario_potencia(self):
        return FormularioPotencia(self.app, "Ingresa Potencia", "Potencia").mostrar_formulario_carga()
    
    def get_formulario_fp(self):
        return FormularioFP(self.app, "Ingresa Factor de potencia", "Numero entre del 0 al 100").mostrar_formulario_carga()
    
    def get_memoria_de_calculo(self):
        return MemoriaDeCalculo(self.app, CalculadoraService()).mostrar_memoria()