from abc import ABC, abstractmethod
from typing import List, Tuple

from data.data import DataList

class FactorAgrupamientoStrategy(ABC):
        @abstractmethod
        def seleccionar(self,hilos: int) -> float:
            pass

class FactorAgrupamiento(FactorAgrupamientoStrategy):
    def __init__(self):
        self.rangos: List[Tuple[int, int, float]] = DataList().get_factorAgrupamiento() 

    
    def seleccionar(self, hilos: int) -> float:
        for rango in self.rangos:
            if rango[0] <= hilos <= rango[1]:
                return rango[2]
        raise ValueError("Número de hilos fuera de rango")

