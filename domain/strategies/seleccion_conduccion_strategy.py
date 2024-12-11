from abc import ABC, abstractmethod

from domain.strategies.factor_temperatura_strategy import FactorTemperatura60A30Cstrategy, FactorTemperatura75A30Cstrategy

class SeleccionConduccionStrategy(ABC):

    @abstractmethod
    def caida_de_tension(self) -> float:
        pass
    
    def capacidad_de_conduccion(self, corriente_nominal: float, hilos: int, temperatura: int, temperatura_cable:int)->float:
        return corriente_nominal /(self.factor_de_agrupamiento(hilos) * self.factor_temperatura(temperatura_cable,temperatura))
    
    def factor_temperatura(self, temperatura_cable: int, temperatura: int) -> float:
        if temperatura_cable == 60:
            seleccionar = FactorTemperatura60A30Cstrategy()
        elif temperatura_cable == 75:
            seleccionar = FactorTemperatura75A30Cstrategy()
        else:
            raise ValueError("Temperatura no soportada")
        return seleccionar.seleccionar(temperatura)
 
    def factor_de_agrupamiento(self, hilos: int) -> float:
        if hilos < 4:
            return 1.0
        elif 4 <= hilos <= 6:
            return 0.8
        elif 7 <= hilos <= 9:
            return 0.7
        elif 10 <= hilos <= 20:
            return 0.5
        elif 21 <= hilos <= 30:
            return 0.45
        elif 31 <= hilos <= 40:
            return 0.4
        elif hilos >= 41:
            return 0.35
        else:
            return 1.0
        
class SeleccionConduccionTrifasicasStrategy(SeleccionConduccionStrategy):
    def caida_de_tension(self):
        return 3.0