from abc import ABC, abstractmethod
import bisect

class CalculoDeInterruptorStrategy(ABC):
    @abstractmethod
    def calcular(self, corriente: float) -> int:
        pass
    
    def seleccionar(self, corriente_nominal: float) -> int:
        lista = [10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 
                  125, 150, 175, 200, 225, 250, 300, 400, 500,
                 600, 700, 800, 1000, 1200, 1600, 2000, 2500, 3200, 4000, 
                 5000, 6300]
        sorted(lista)
        interruptor = bisect.bisect_left(lista, corriente_nominal)
        return lista[interruptor] if interruptor < len(lista) else 0


class AlimentadorStrategy(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> int:
        return self.seleccionar(corriente * 1.25)
    

class MotorStrategy(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> int:
        return self.seleccionar(corriente * 2)


class FiltroStrategy(CalculoDeInterruptorStrategy):
    def calcular(self, corriente: float) -> int:
        return self.seleccionar(corriente * 1.35)
