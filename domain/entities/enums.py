from enum import Enum

class TipoCircuito(Enum):
    ESTRELLA = "Estrella"
    DELTA = "Delta"
    #BIFASICO = "Bifásico"
    #MONOFASICO = "Monofásico"

class TensionEnvoltaje(Enum):
    
    V127 = "127V"
    V220 = "220V"
    V440 = "440V"
    V480 = "480V"
    V13KV = "13.2KV"
    V23KV = "23KV"
    V34KV = "34.5KV"

class TipoCarga(Enum):
    ALIMENTADOR = "Alimentador"
    MOTOR = "Motor"
    FILTRO = "Filtro"
    INTERRUPTOR_MANUAL = "Interruptor Manual"

class TipoMaterialCable(Enum):
    COBRE = "Cobre"
    ALUMINIO = "Aluminio"

class Canalizacion(Enum):
    TUBERIA = "Tubería"
    CHAROLA = "Charola"
    
class Tuberia(Enum):
    PVC = "PVC"
    PG = "Pared Gruesa"
    PD = "Pared Delgada"

class Charola(Enum):
    ESCALERA = "Tipo Escalera"
    MALLA = "Tipo Malla"
    FONDO_SOLIDO = "Fondo Solido"

class TablaNormaSeleccionCable(Enum):
    TUBERIA = "310-15(b)(16)"
    CHAROLA_ARREGLO_TRIANGULAR = "310-15(b)(20)"
    CHAROLA_ARREGLO_CABLES_SEPARADO = "310-15(b)(17)"
    MAS_2000V_INDIVIDUAL = "310-60(69)"
    MAS_2000V_TRIANGULAR = "310-60(C)(67)"