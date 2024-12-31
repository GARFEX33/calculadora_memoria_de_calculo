from abc import ABC, abstractmethod
from data.data import DataList

class FactorTemperaturaStrategy(ABC):
        @abstractmethod
        def seleccionar(self,temperatura_ambiente: int) -> float:
            pass

class FactorTemperatura60A30Cstrategy(FactorTemperaturaStrategy):
    def __init__(self):
        # Rango de temperaturas y factores para cables de 60°C
        self.rangos = DataList().get_factorTemperatura60A30C()
  
    def seleccionar(self, temperatura_ambiente: int) -> float:
        # Buscar en qué rango está la temperatura
        for rango in self.rangos:
            if rango[0] <= temperatura_ambiente <= rango[1]:
                return rango[2]
        raise ValueError("Temperatura fuera de rango para cables de 60°C")
    
class FactorTemperatura75A30Cstrategy(FactorTemperaturaStrategy):
    def __init__(self):
            self.rangos = DataList().get_factorTemperatura75A30C()

    def seleccionar(self, temperatura_ambiente: int) -> float:
        for rango in self.rangos:
            if rango[0] <= temperatura_ambiente <= rango[1]:
                return rango[2]
        raise ValueError("Temperatura fuera de rango para cables de 75°C")



