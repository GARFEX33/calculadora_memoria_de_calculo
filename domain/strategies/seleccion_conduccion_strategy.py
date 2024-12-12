from abc import ABC, abstractmethod
from typing import Tuple

from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion
from domain.strategies.factor_agrupamiento_strategy import FactorAgrupamiento
from domain.strategies.factor_temperatura_strategy import FactorTemperatura60A30Cstrategy, FactorTemperatura75A30Cstrategy
from domain.strategies.seleccionar_cable_strategy import SeleccionarCableCobreTemp60Tubo, SeleccionarCableCobreTemp75Tubo

class SeleccionConduccionStrategy(ABC):

    @abstractmethod
    def caida_de_tension(self) -> float:
        pass
    
    def seleccionar_cable(self, carga: Carga, canalizacion: Canalizacion) -> Tuple[str, int]:
        if carga.corriente_nominal < 100 and canalizacion == Canalizacion.TUBERIA:
            seleccionar = SeleccionarCableCobreTemp60Tubo()
        elif carga.corriente_nominal >= 200 and canalizacion == Canalizacion.TUBERIA:   
            seleccionar = SeleccionarCableCobreTemp75Tubo()
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
