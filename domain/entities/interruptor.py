from pydantic import BaseModel, ConfigDict
from enum import Enum
from domain.strategies.calculo_interruptor_strategy import AlimentadorStrategy, CalculoDeInterruptorStrategy

class CapacidadCortoCircuito(Enum):
    KA_5 = 5
    KA_10 = 10
    KA_15 = 15
    KA_20 = 20
    KA_25 = 25
    KA_30 = 30
    KA_35 = 35


class Interruptor(BaseModel):
    bornes: int = 0
    ampacidad: int = 0
    capacidad_corto_circuito: CapacidadCortoCircuito = CapacidadCortoCircuito.KA_20
    calcular_tipo_carga: CalculoDeInterruptorStrategy = AlimentadorStrategy()
    model_config = ConfigDict(arbitrary_types_allowed=True)

    def seleccionar_interruptor(self, corriente: float ) -> 'Interruptor':
         self.ampacidad, self.bornes  = self.calcular_tipo_carga.calcular(corriente)
         return self   
    


