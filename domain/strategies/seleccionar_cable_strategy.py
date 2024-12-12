from abc import ABC, abstractmethod
from typing import List, Tuple

from data.data import DataList
from domain.entities.carga import Carga

class SeleccionarCableStrategy(ABC):
        @abstractmethod
        def seleccionar(self,carga: Carga) -> Tuple[str, int]:
            pass
class SeleccionarCableCobreTemp60Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp60Tubo()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 60°C")
    
class SeleccionarCableCobreTemp75Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]]  = DataList().get_ampacidadCobreTemp75Tubo()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")
    




