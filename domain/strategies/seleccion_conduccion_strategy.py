from abc import ABC, abstractmethod

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
    
    def seleccionar_cable(self, carga: Carga, cable: Cable, canalizacion: Canalizacion, numero_de_hilos_por_fase:int) -> Cable:
        if carga.corriente_nominal < 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE and numero_de_hilos_por_fase == 1:
            seleccionar = SeleccionarCableCobreTemp60Tubo(cable)
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE and numero_de_hilos_por_fase >= 1:   
            seleccionar = SeleccionarCableCobreTemp75Tubo(cable)
        elif carga.corriente_nominal < 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO and numero_de_hilos_por_fase == 1:
            seleccionar = SeleccionarCableAluminioTemp60Tubo(cable)
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.TUBERIA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO and numero_de_hilos_por_fase >= 1:
            seleccionar = SeleccionarCableAluminioTemp75Tubo(cable)
        elif carga.corriente_nominal < 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE and numero_de_hilos_por_fase == 1:
            seleccionar = SeleccionarCableCobreTemp60Charola(cable)
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE and numero_de_hilos_por_fase == 1:
            seleccionar = SeleccionarCableCobreTemp75Charola(cable)
        elif carga.corriente_nominal < 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO and numero_de_hilos_por_fase== 1:
            seleccionar = SeleccionarCableAluminioTemp60Charola(cable)
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO and numero_de_hilos_por_fase == 1:
            seleccionar = SeleccionarCableAluminioTemp75Charola(cable)
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.COBRE and numero_de_hilos_por_fase > 1:
            seleccionar = SeleccionarCableCobreTemp75CharolaTriangular(cable)
        elif carga.corriente_nominal >= 100 and canalizacion == Canalizacion.CHAROLA and carga.tension < 2000 and cable.material == TipoMaterialCable.ALUMINIO and numero_de_hilos_por_fase > 1:
            seleccionar = SeleccionarCableAluminioTemp75CharolaTriangular(cable)

        else:    
            raise NotImplementedError("Este método debe ser implementado por las subclases")
        return seleccionar.seleccionar(carga)  # type: ignore
    
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
