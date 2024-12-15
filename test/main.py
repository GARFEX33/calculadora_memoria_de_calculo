from application.calculadora_service import CalculadoraService
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoCarga, TipoCircuito
from domain.entities.interruptor import Interruptor


def main():
    carga = Carga(
        tension = 220,
        potencia = 20,
        factor_potencia = 1,
        tipo_circuito = TipoCircuito.DELTA,
        tipo_carga = TipoCarga.ALIMENTADOR, 
        )
    canalizacion = Canalizacion.TUBERIA
    interruptor = Interruptor(
        bornes=1,
        ampacidad= 100,
    )
    cable = Cable(
        temperatura= 75,
    )
    servicio = CalculadoraService()
    servicio.calcular_amperaje(carga)
    carga.capacidad_conduccion = servicio.seleccion_de_cable_por_capacidad_de_conduccion(carga, cable, opcion = "1")
    lista  = servicio.lista_de_cables_seleccionados(carga, interruptor, cable, canalizacion, opcion = "1")
    print("Lista de cables seleccionados")
    print(lista.__str__())
    print(carga.capacidad_conduccion)


if __name__ == "__main__":
    main()
