# domain/strategies/calculadora_amperaje_strategy.py

from abc import ABC, abstractmethod
from math import sqrt
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class CalculoCaidaDeTensionStrategy(ABC):
    def __init__(self,app: "CalculadoraGARFEX") -> None:
        self.app = app

    @abstractmethod
    def calcular_caida(self) -> float:
        pass


class CaidaTrifasica(CalculoCaidaDeTensionStrategy):
    def calcular_caida(self) -> float:
        if self.app.cable.mm2 is None:
            self.app.cable.mm2 = 0
        result : float = (2 * sqrt(3) * self.app.carga.longitud * self.app.carga.corriente_nominal) / ( self.app.carga.tension * self.app.cable.mm2) 
        return result


# class CaidaBifasica(CalculoCaidaDeTensionStrategy):
#     def calcular_amperaje(self) -> float:
#         return potencia / (2 * (voltaje/1000) * sqrt(3) * factor_potencia)


# class CaidaMonofasica(CalculoCaidaDeTensionStrategy):
#     def calcular_amperaje(self, potencia: float, voltaje: float, factor_potencia: float) -> float:
#         return potencia / ((voltaje/1000) * factor_potencia)
