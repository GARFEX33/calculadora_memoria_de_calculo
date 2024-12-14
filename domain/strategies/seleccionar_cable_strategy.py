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
    
class SeleccionarCableCobreTemp90Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp90Tubo()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C")

class SeleccionarCableAluminioTemp60Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp60Tubo()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 60°C")

class SeleccionarCableAluminioTemp75Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp75Tubo()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")

class SeleccionarCableAluminioTemp90Tubo(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp90Tubo()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C") 

class SeleccionarCableCobreTemp60Charola(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp60Charola()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 60°C")

class SeleccionarCableCobreTemp75Charola(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp75Charola()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")
    
class SeleccionarCableCobreTemp90Charola(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadCobreTemp90Charola()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C")

class SeleccionarCableAluminioTemp60Charola(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp60Charola()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 60°C")

class SeleccionarCableAluminioTemp75Charola(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp75Charola()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")

class SeleccionarCableAluminioTemp90Charola(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidadAluminioTemp90Charola()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C")

class SeleccionarCableCobreTemp75CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_aluminio_75C_a_40C_charola_triangular()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")

class SeleccionarCableCobreTemp90CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_aluminio_90C_a_40C_charola_triangular()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C")

class SeleccionarCableAluminioTemp75CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_aluminio_75C_a_40C_charola_triangular()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 75°C")

class SeleccionarCableAluminioTemp90CharolaTriangular(SeleccionarCableStrategy):
    def __init__(self):
        self.rangos: List[Tuple[str, int]] = DataList().get_ampacidad_aluminio_90C_a_40C_charola_triangular()

    def seleccionar(self, carga: Carga) -> Tuple[str, int]:
        # Buscar
        for rango in self.rangos:
            if carga.capacidad_conduccion <= rango[1]:
                return rango
        raise ValueError("Temperatura fuera de rango para cables de 90°C")