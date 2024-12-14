# application/calculadora_service.py

from typing import Tuple
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoSistema

from domain.strategies.seleccion_conduccion_strategy import  SeleccionConduccionTrifasicaITMStrategy, SeleccionConduccionTrifasicaStrategy


class CalculadoraService:

    def calcular_amperaje(self, carga: Carga):
        return carga.calcular_amperaje()
    
    def seleccionar_interruptor(self, carga: Carga):
        return carga.seleccionar_interruptor()
    
    def seleccion_de_cable_por_capacidad_de_conduccion(self, tipo_sistema: TipoSistema, carga: Carga, cable:Cable, opcion:str) -> float:
        
        if tipo_sistema == TipoSistema.ESTRELLA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(cable, carga)
        elif tipo_sistema == TipoSistema.ESTRELLA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(cable, carga)
        elif tipo_sistema == TipoSistema.DELTA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(cable, carga)
        elif tipo_sistema == TipoSistema.DELTA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(cable, carga)
        # elif tipo_sistema == TipoSistema.BIFASICO:
        #     return BifasicoCalculadora()
        # elif tipo_sistema == TipoSistema.MONOFASICO:
        #     return MonofasicoCalculadora()
        else:
            raise ValueError("Tipo de sistema no válido")
    
    def selecionar_cable(self, carga: Carga,cable: Cable, canalizacion: Canalizacion, tipo_sistema: TipoSistema, opcion:str) -> Tuple[str, int]:
        
        if tipo_sistema == TipoSistema.ESTRELLA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().seleccionar_cable(carga, cable ,canalizacion)
        elif tipo_sistema == TipoSistema.ESTRELLA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().seleccionar_cable(carga, cable, canalizacion)
        elif tipo_sistema == TipoSistema.DELTA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().seleccionar_cable(carga, cable, canalizacion)
        elif tipo_sistema == TipoSistema.DELTA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().seleccionar_cable(carga, cable, canalizacion)
        else:
            raise ValueError("Tipo de sistema no válido")
