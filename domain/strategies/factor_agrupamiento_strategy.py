from abc import ABC, abstractmethod

class FactorAgrupamientoStrategy(ABC):
        @abstractmethod
        def seleccionar(self,hilos: int) -> float:
            pass

class FactorAgrupamiento(FactorAgrupamientoStrategy):
    def __init__(self):
        self.rangos: list[tuple[int, int, float]]= [
            (1, 3, 1.0),
            (4, 6, 0.8),
            (7, 9, 0.7),
            (10, 20, 0.5),
            (21, 30, 0.45),
            (31, 40, 0.4),
            (41, int('inf'), 0.35) 
        ]
    
    def seleccionar(self, hilos: int) -> float:
        for rango in self.rangos:
            if rango[0] <= hilos <= rango[1]:
                return rango[2]
        raise ValueError("Número de hilos fuera de rango")

