from abc import ABC, abstractmethod

class FactorTemperaturaStrategy(ABC):
        @abstractmethod
        def seleccionar(self,temperatura_ambiente: int) -> float:
            pass

class FactorTemperatura60A30Cstrategy(FactorTemperaturaStrategy):
    def __init__(self):
        # Rango de temperaturas y factores para cables de 60°C
        self.rangos = [
            (1, 10, 1.29),
            (11, 15, 1.22),
            (16, 20, 1.15),
            (21, 25, 1.08),
            (26, 30, 1.0),
            (31, 35, 0.91),
            (36, 40, 0.82),
            (41, 45, 0.71),
            (46, 50, 0.58),
            (51, 55, 0.41)
        ]
  
    def seleccionar(self, temperatura_ambiente: int) -> float:
        # Buscar en qué rango está la temperatura
        for rango in self.rangos:
            if rango[0] <= temperatura_ambiente <= rango[1]:
                return rango[2]
        raise ValueError("Temperatura fuera de rango para cables de 60°C")
    
class FactorTemperatura75A30Cstrategy(FactorTemperaturaStrategy):
    def __init__(self):
        # Rango de temperaturas y factores para cables de 75°C
            self.rangos = [
            (1, 10, 1.2),
            (11, 15, 1.15),
            (16, 20, 1.11),
            (21, 25, 1.05),
            (26, 30, 1.0),
            (31, 35, 0.94),
            (36, 40, 0.88),
            (41, 45, 0.82),
            (46, 50, 0.75),
            (51, 55, 0.67),
            (56, 60, 0.58),
            (61, 65, 0.47)
        ]

  
    def seleccionar(self, temperatura_ambiente: int) -> float:
        # Buscar en qué rango está la temperatura
        for rango in self.rangos:
            if rango[0] <= temperatura_ambiente <= rango[1]:
                return rango[2]
        raise ValueError("Temperatura fuera de rango para cables de 75°C")



