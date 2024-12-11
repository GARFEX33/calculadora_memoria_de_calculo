from enum import Enum


class TipoSistema(Enum):
    TRIFASICO = "Trifásico"
    #BIFASICO = "Bifásico"
    #MONOFASICO = "Monofásico"

class TipoCarga(Enum):
    ALIMENTADOR = "Alimentador"
    MOTOR = "Motor"
    FILTRO = "Filtro"