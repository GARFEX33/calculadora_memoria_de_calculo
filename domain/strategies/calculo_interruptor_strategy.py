from abc import ABC, abstractmethod
from typing import List, Tuple

from data.data import DataList

class CalculoDeInterruptorStrategy(ABC):
    @abstractmethod
    def calcular(self, corriente: float) -> Tuple[int, int]:
        pass
    
    def seleccionar(self, corriente_nominal: float) -> Tuple[int, int]:
        print(f"Corriente nominal para interruptor: {corriente_nominal}")
        rangos: List[Tuple[int, int]] = DataList().get_lista_de_interruptores()

        for rango in rangos:
            if corriente_nominal <= rango[0]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C")


class AlimentadorStrategy(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> Tuple[int, int]:
        return self.seleccionar(corriente * 1.25)
    

class MotorStrategy(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> Tuple[int, int]:
        return self.seleccionar(corriente * 2)


class FiltroStrategy(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> Tuple[int, int]:
        return self.seleccionar(corriente * 1.35)
