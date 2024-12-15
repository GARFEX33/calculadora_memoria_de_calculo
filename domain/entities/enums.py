from enum import Enum

class TipoCircuito(Enum):
    ESTRELLA = "Estrella"
    DELTA = "Delta"
    #BIFASICO = "Bifásico"
    #MONOFASICO = "Monofásico"

class TipoCarga(Enum):
    ALIMENTADOR = "Alimentador"
    MOTOR = "Motor"
    FILTRO = "Filtro"

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