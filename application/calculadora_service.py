# application/calculadora_service.py

from domain.entities.carga import Carga
from domain.entities.enums import TipoCarga, TipoSistema
from domain.strategies.calculadora_amperaje_strategy import (
    CalculadoraAmperajeStrategy,
    TrifasicoCalculadora,
    BifasicoCalculadora,
    MonofasicoCalculadora,
)
from domain.strategies.calculo_interruptor_strategy import AlimentadorStrategy, FiltroStrategy, MotorStrategy


class CalculadoraService:

    def calcular_amperaje(self, carga: Carga):
        return carga.calcular_amperaje()
    
    def tipo_de_sistema_selector(self, tipo_sistema: TipoSistema) -> CalculadoraAmperajeStrategy:
        if tipo_sistema == TipoSistema.TRIFASICO:
            return TrifasicoCalculadora()
        elif tipo_sistema == TipoSistema.BIFASICO:
            return BifasicoCalculadora()
        elif tipo_sistema == TipoSistema.MONOFASICO:
            return MonofasicoCalculadora()
        else:
            raise ValueError("Tipo de sistema no válido")
        
    def tipo_de_carga_selector(self, tipo_carga: TipoCarga):

        if tipo_carga == TipoCarga.ALIMENTADOR:
            return AlimentadorStrategy()
        elif tipo_carga == TipoCarga.MOTOR:
            return MotorStrategy()
        elif tipo_carga == TipoCarga.FILTRO:
            return FiltroStrategy()
        else:
            raise ValueError("Tipo de carga no válida")
    
    def seleccionar_interruptor(self, carga: Carga):
        return carga.seleccionar_interruptor()
    
#    def seleccion_de_cable_por_capacidad_de_conduccion(self):
#        return SeleccionConduccionTrifasicasStrategy()