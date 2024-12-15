from abc import ABC, abstractmethod
from typing import List, Tuple

from data.data import DataList

class CalculoDeInterruptorStrategy(ABC):
    @abstractmethod
    def calcular(self, corriente: float) -> Tuple[int, int]:
        pass
    
    def seleccionar(self, corriente_nominal: float) -> Tuple[int, int]:
        rangos: List[Tuple[int, int]] = DataList().get_lista_de_interruptores()

        for rango in rangos:
            if corriente_nominal <= rango[0]:
                print(f"Interruptor termomagnético seleccionado: {rango[1]}X{rango[0]}A")
                print(f"Corriente nominal: {corriente_nominal:.2f} A")
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

class SeleccionInterruptor(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> Tuple[int, int]:
        print("Seleccion de interruptor en calcular")
        return self.seleccionar(corriente)