# domain/entities/sistema.py

from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, ConfigDict

from domain.entities.enums import TipoCarga, TipoCircuito
from domain.strategies.calculadora_amperaje_strategy import CalculadoraAmperajeStrategy, TrifasicoCalculadora
from domain.strategies.calculo_caida_de_tension_strategy import CaidaTrifasica, CalculoCaidaDeTensionStrategy
if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX

class Carga(BaseModel):
    nombre: str = ""
    tipo_circuito: TipoCircuito = TipoCircuito.ESTRELLA
    tipo_carga: TipoCarga = TipoCarga.ALIMENTADOR
    potencia: float = 0
    tension: float = 0
    factor_potencia: float = 1
    corriente_nominal: float = 0
    hilos: int = 3
    longitud: float = 0
    caida_tension: float = 0
    temperatura_ambiente: int = 30
    capacidad_conduccion: float = 0
    calcular_circuito: CalculadoraAmperajeStrategy  = TrifasicoCalculadora()
    caida_de_tension_strategy: Optional[CalculoCaidaDeTensionStrategy] = None

        # Configuración para permitir tipos arbitrarios
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def calcular_amperaje(self):
     self.corriente_nominal = self.calcular_circuito.calcular_amperaje(self.potencia, self.tension, self.factor_potencia)
    
    def calcular_caida_de_tension(self, app: "CalculadoraGARFEX"):
        if self.tipo_circuito == TipoCircuito.ESTRELLA or self.tipo_circuito == TipoCircuito.DELTA:
            self.caida_de_tension_strategy = CaidaTrifasica(app)
            self.caida_tension = self.caida_de_tension_strategy.calcular_caida( )
        else:    
            raise ValueError("Tipo de sistema no válido")