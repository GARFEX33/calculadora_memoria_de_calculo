# domain/strategies/calculadora_amperaje_strategy.py

from abc import ABC, abstractmethod
from math import sqrt


class CalculadoraAmperajeStrategy(ABC):
    @abstractmethod
    def calcular_amperaje(self, potencia: float, voltaje: float, factor_potencia: float) -> float:
        pass

class TrifasicoCalculadora(CalculadoraAmperajeStrategy):
    def calcular_amperaje(self, potencia: float, voltaje: float, factor_potencia: float) -> float:
        return potencia / ((voltaje/1000) * sqrt(3) * factor_potencia)


class BifasicoCalculadora(CalculadoraAmperajeStrategy):
    def calcular_amperaje(self, potencia: float, voltaje: float, factor_potencia: float) -> float:
        return potencia / (2 * (voltaje/1000) * sqrt(3) * factor_potencia)


class MonofasicoCalculadora(CalculadoraAmperajeStrategy):
    def calcular_amperaje(self, potencia: float, voltaje: float, factor_potencia: float) -> float:
        return potencia / ((voltaje/1000) * factor_potencia)
