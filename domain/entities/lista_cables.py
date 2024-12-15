from pydantic import BaseModel

from domain.entities.cable import Cable

class CableSelecciondo(BaseModel):
    cable: Cable = Cable()
    cable_por_fase: int = 0
    total_costo: float = 0.0

