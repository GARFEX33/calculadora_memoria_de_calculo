from abc import ABC
from typing import List, Tuple

from data.data import DataList
from domain.entities.cable import Cable

class SeleccionarSeccionDeCableStrategy(ABC):
        def __init__(self, cable: Cable):
            self.rangos: List[Tuple[str, float]] = []
            self.cable: Cable = cable
        
        def seleccionar(self)-> float | None:
            for rango in self.rangos:
                if self.cable.calibre == rango[0]:
                    self.cable.calibre = rango[0]
                    self.cable.mm2 = rango[1]
                    return self.cable.mm2
            return None
        
class SeleccionarSeccionDeCable(SeleccionarSeccionDeCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos = DataList().get_seccion_conductor()

