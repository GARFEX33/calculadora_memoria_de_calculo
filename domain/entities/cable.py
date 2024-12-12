from pydantic import BaseModel


class Cable(BaseModel):
    calibre: str
    temperatura: int
    amperaje: int
    # mm2: float
    # diametro: float
    # material: str
    # resistencia: float
    # area_conductor_con_aislamiento: float
    # area_conductor_sin_aislamiento: float

    def seleccionar_temperatura_cable(self, amperaje: float):
        self.temperatura = 60 if amperaje < 100 else 75
    
    

