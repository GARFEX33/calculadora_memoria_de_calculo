from pydantic import BaseModel

from domain.entities.enums import TipoMaterialCable


class Cable(BaseModel):
    calibre: str = ""
    temperatura: int = 0
    amperaje: int = 0
    material: TipoMaterialCable = TipoMaterialCable.COBRE
    # mm2: float
    # diametro: float
    # resistencia: float
    # area_conductor_con_aislamiento: float
    # area_conductor_sin_aislamiento: float
    costo: float = 0.0

    def seleccionar_temperatura_cable(self, amperaje: float):
        self.temperatura = 60 if amperaje < 100 else 75
    
    


