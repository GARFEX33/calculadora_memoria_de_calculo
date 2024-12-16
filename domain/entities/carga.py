# domain/entities/sistema.py

from pydantic import BaseModel, ConfigDict

from domain.entities.enums import TipoCarga, TipoCircuito
from domain.strategies.calculadora_amperaje_strategy import CalculadoraAmperajeStrategy, TrifasicoCalculadora

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
    
        # Configuración para permitir tipos arbitrarios
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def calcular_amperaje(self):
     self.corriente_nominal = self.calcular_circuito.calcular_amperaje(self.potencia, self.tension, self.factor_potencia)

      
