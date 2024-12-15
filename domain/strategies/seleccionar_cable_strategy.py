from abc import ABC
from typing import List, Tuple

from data.data import DataList
from domain.entities.cable import Cable
from domain.entities.carga import Carga

class SeleccionarCableStrategy(ABC):
        def __init__(self, cable: Cable):
            self.rangos: List[Tuple[str, int]] = []
            self.cable: Cable = cable
        
        def seleccionar(self,carga: Carga)-> Cable | None:
            for rango in self.rangos:
                if carga.capacidad_conduccion <= rango[1]:
                    self.cable.calibre = rango[0]
                    self.cable.amperaje = rango[1]
                    return self.cable
            return None

class SeleccionarCableCobreTemp60Tubo(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos = DataList().get_ampacidadCobreTemp60Tubo()

  
class SeleccionarCableCobreTemp75Tubo(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]]  = DataList().get_ampacidadCobreTemp75Tubo()
 
class SeleccionarCableCobreTemp90Tubo(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp90Tubo()
       
class SeleccionarCableAluminioTemp60Tubo(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp60Tubo()

class SeleccionarCableAluminioTemp75Tubo(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp75Tubo()

class SeleccionarCableAluminioTemp90Tubo(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp90Tubo()

class SeleccionarCableCobreTemp60Charola(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp60Charola()

class SeleccionarCableCobreTemp75Charola(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp75Charola()
 
class SeleccionarCableCobreTemp90Charola(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp90Charola()

class SeleccionarCableAluminioTemp60Charola(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp60Charola()

class SeleccionarCableAluminioTemp75Charola(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp75Charola()

class SeleccionarCableAluminioTemp90Charola(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp90Charola()

class SeleccionarCableCobreTemp75CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_cobre_75C_a_40C_charola_triangular()

class SeleccionarCableCobreTemp90CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_cobre_90C_a_40C_charola_triangular()

class SeleccionarCableAluminioTemp75CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_aluminio_75C_a_40C_charola_triangular()

class SeleccionarCableAluminioTemp90CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self,cable: Cable):
        super().__init__(cable) 
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_aluminio_90C_a_40C_charola_triangular()

