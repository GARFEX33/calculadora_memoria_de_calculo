# application/calculadora_service.py

from typing import Tuple
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoCarga, TipoSistema
from domain.strategies.calculadora_amperaje_strategy import (
    CalculadoraAmperajeStrategy,
    TrifasicoCalculadora,
    BifasicoCalculadora,
    MonofasicoCalculadora,
)
from domain.strategies.calculo_interruptor_strategy import AlimentadorStrategy, FiltroStrategy, MotorStrategy
from domain.strategies.seleccion_conduccion_strategy import  SeleccionConduccionTrifasicaITMStrategy, SeleccionConduccionTrifasicaStrategy


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
    
    def seleccion_de_cable_por_capacidad_de_conduccion(self, tipo_sistema: TipoSistema, carga: Carga, cable:Cable, opcion:str) -> float:
        
        if tipo_sistema == TipoSistema.TRIFASICO and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(cable, carga)
        elif tipo_sistema == TipoSistema.TRIFASICO and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(cable, carga)
        
        # elif tipo_sistema == TipoSistema.BIFASICO:
        #     return BifasicoCalculadora()
        # elif tipo_sistema == TipoSistema.MONOFASICO:
        #     return MonofasicoCalculadora()
        else:
            raise ValueError("Tipo de sistema no válido")
    
    def selecionar_cable(self, carga: Carga, canalizacion: Canalizacion, tipo_sistema: TipoSistema, opcion:str) -> Tuple[str, int]:
        if tipo_sistema == TipoSistema.TRIFASICO and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().seleccionar_cable(carga, canalizacion)
        elif tipo_sistema == TipoSistema.TRIFASICO and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().seleccionar_cable(carga, canalizacion)
        else:
            raise ValueError("Tipo de sistema no válido")
