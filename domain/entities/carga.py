# domain/entities/sistema.py

from pydantic import BaseModel, ConfigDict
from domain.strategies.calculadora_amperaje_strategy import CalculadoraAmperajeStrategy
from domain.strategies.calculo_interruptor_strategy import CalculoDeInterruptorStrategy

class Carga(BaseModel):
    nombre: str
    tipo_circuito: CalculadoraAmperajeStrategy
    tipo_carga: CalculoDeInterruptorStrategy
    potencia: float
    tension: float
    factor_potencia: float
    corriente_nominal: float = 0
    hilos: int = 4
    longitud: float = 0
    caida_tension: float = 0
    interruptor: int = 0
    temperatura_ambiente: int = 30
    capacidad_conduccion: float = 0
    
        # Configuración para permitir tipos arbitrarios
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def calcular_amperaje(self):
        self.corriente_nominal = self.tipo_circuito.calcular_amperaje(self.potencia, self.tension, self.factor_potencia)
        
    def seleccionar_interruptor(self):
        self.interruptor  = self.tipo_carga.calcular(self.corriente_nominal)