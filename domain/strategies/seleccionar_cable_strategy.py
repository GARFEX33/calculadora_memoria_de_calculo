from abc import ABC, abstractmethod
from typing import Tuple

from domain.entities.carga import Carga

class SeleccionarCableStrategy(ABC):
        @abstractmethod
        def seleccionar(self,carga: Carga) -> Tuple[str, int]:
            pass
class SeleccionarCableCobreTemp60Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos = [
        ("14", 15),
        ("12", 20),
        ("10", 30),
        ("8", 40),
        ("6", 55),
        ("4", 70),
        ("3", 85),
        ("2", 95),
        ("1", 110),
                    ]

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 60°C")
    
class SeleccionarCableCobreTemp75Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos = [
    ("14", 20),
    ("12", 25),
    ("10", 35),
    ("8", 50),
    ("6", 65),
    ("4", 85),
    ("2", 115),
    ("1/0", 150),
    ("2/0", 175),
    ("3/0", 200),
    ("4/0", 230),
    ("250", 255),
    ("300", 285),
    ("350", 310),
    ("400", 335),
    ("500", 380),
    ("600", 420),
    ("750", 475),
    ("1000", 545)
                    ]

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")
    




