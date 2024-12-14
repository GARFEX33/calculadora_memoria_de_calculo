from abc import ABC, abstractmethod
from typing import Tuple

from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoMaterialCable
from domain.strategies.factor_agrupamiento_strategy import FactorAgrupamiento
from domain.strategies.factor_temperatura_strategy import FactorTemperatura60A30Cstrategy, FactorTemperatura75A30Cstrategy
from domain.strategies.seleccionar_cable_strategy import *

class SeleccionConduccionStrategy(ABC):

    @abstractmethod
    def caida_de_tension(self) -> float:
        pass
    
    def seleccionar_cable(self, carga: Carga, cable: Cable, canalizacion: Canalizacion) -> Tuple[str, int]:
        
        if carga.corriente_nominal < 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE:
            seleccionar = SeleccionarCableCobreTemp60Tubo()
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE:   
            seleccionar = SeleccionarCableCobreTemp75Tubo()
        elif carga.corriente_nominal < 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO:
            seleccionar = SeleccionarCableAluminioTemp60Tubo()
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO:
            seleccionar = SeleccionarCableAluminioTemp75Tubo()
        elif carga.corriente_nominal < 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE:
            seleccionar = SeleccionarCableCobreTemp60Charola()
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE:
            seleccionar = SeleccionarCableCobreTemp75Charola()
        elif carga.corriente_nominal < 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO:
            seleccionar = SeleccionarCableAluminioTemp60Charola()
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO:
            seleccionar = SeleccionarCableAluminioTemp75Charola()
        
        
        else:    
            raise NotImplementedError("Este método debe ser implementado por las subclases")
        return seleccionar.seleccionar(carga)
    
    def capacidad_de_conduccion(self, cable:Cable, carga: Carga)->float:
        return carga.corriente_nominal /(self.factor_de_agrupamiento(carga.hilos) * self.factor_temperatura(cable, carga))
    
    def factor_temperatura(self, cable: Cable, carga: Carga) -> float:
        if cable.temperatura == 60:
            seleccionar = FactorTemperatura60A30Cstrategy()
        elif cable.temperatura == 75:
            seleccionar = FactorTemperatura75A30Cstrategy()
        else:
            raise ValueError("Temperatura no soportada")
        return seleccionar.seleccionar(carga.temperatura_ambiente)
 
    def factor_de_agrupamiento(self, hilos: int) -> float:
        return FactorAgrupamiento().seleccionar(hilos)

class SeleccionConduccionTrifasicaStrategy(SeleccionConduccionStrategy):
    def caida_de_tension(self):
        return 3.0

class SeleccionConduccionTrifasicaITMStrategy(SeleccionConduccionStrategy):
    def caida_de_tension(self):
        return 3.0
    def capacidad_de_conduccion(self, cable:Cable, carga: Carga)->float:
        return carga.corriente_nominal
