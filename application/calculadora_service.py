from copy import deepcopy
from typing import List, Tuple
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoCarga, TipoCircuito

from domain.entities.interruptor import Interruptor
from domain.strategies.calculo_interruptor_strategy import AlimentadorStrategy, CalculoDeInterruptorStrategy, FiltroStrategy, MotorStrategy, SeleccionInterruptor
from domain.strategies.seleccion_conduccion_strategy import  SeleccionConduccionTrifasicaITMStrategy, SeleccionConduccionTrifasicaStrategy


class CalculadoraService:

    def calcular_amperaje(self, carga: Carga):
        return carga.calcular_amperaje()
    
    def seleccionar_interruptor(self, carga: Carga, interruptor: Interruptor) -> Interruptor:
        return interruptor.seleccionar_interruptor(carga.corriente_nominal)
    
    def seleccionar_tipo_de_carga(self, carga: Carga)-> CalculoDeInterruptorStrategy:
        if carga.tipo_carga == TipoCarga.ALIMENTADOR:
            return AlimentadorStrategy()
        elif carga.tipo_carga == TipoCarga.MOTOR:
            return MotorStrategy()
        elif carga.tipo_carga == TipoCarga.FILTRO:
            return FiltroStrategy()
        elif carga.tipo_carga == TipoCarga.INTERRUPTOR_MANUAL:
            return SeleccionInterruptor()
            
        else:
            raise ValueError("Tipo de carga no válido")
    
    def seleccion_de_cable_por_capacidad_de_conduccion(self, carga: Carga, cable:Cable, opcion:str) -> float:

        if carga.tipo_circuito == TipoCircuito.ESTRELLA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(cable, carga)
        elif carga.tipo_circuito == TipoCircuito.ESTRELLA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(cable, carga)
        elif carga.tipo_circuito == TipoCircuito.DELTA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(cable, carga)
        elif carga.tipo_circuito == TipoCircuito.DELTA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(cable, carga)
        # elif tipo_sistema == TipoSistema.BIFASICO:
        #     return BifasicoCalculadora()
        # elif tipo_sistema == TipoSistema.MONOFASICO:
        #     return MonofasicoCalculadora()
        else:
            raise ValueError("Tipo de sistema no válido")
    
    def selecionar_cable(self, carga: Carga, cable: Cable, canalizacion: Canalizacion, opcion:str, interruptor: Interruptor) -> Cable:

        if carga.tipo_circuito == TipoCircuito.ESTRELLA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().seleccionar_cable(carga, cable ,canalizacion, interruptor.bornes)
        elif carga.tipo_circuito == TipoCircuito.ESTRELLA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().seleccionar_cable(carga, cable, canalizacion, interruptor.bornes)
        elif carga.tipo_circuito == TipoCircuito.DELTA and opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().seleccionar_cable(carga, cable, canalizacion,interruptor.bornes)
        elif carga.tipo_circuito == TipoCircuito.DELTA and opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().seleccionar_cable(carga, cable, canalizacion, interruptor.bornes)
        else:
            raise ValueError("Tipo de sistema no válido")

    def seleccionar_numero_hilos_interruptor(self, tipo_sistema: TipoCircuito)->int:
        if tipo_sistema.ESTRELLA or tipo_sistema.DELTA:
            hilos = 3
        else:
            hilos = 1
        return hilos
    
    def lista_de_cables_seleccionados(self, carga: Carga, interruptor: Interruptor, cable: Cable, canalizacion: Canalizacion,  opcion:str)-> List[ Tuple[(int,Cable)] ]:
        cables: List[ Tuple[(int,Cable)] ]= []
        for i in range(interruptor.bornes):
            # Crea una copia del objeto carga
            carga_copia = deepcopy(carga)
            carga_copia.capacidad_conduccion = carga.capacidad_conduccion / (i + 1)
            cable_copia = deepcopy(cable)
            
            # Llama a seleccionar_cable y crea un nuevo Cable si es necesario
            cable_encontrado = self.selecionar_cable(carga_copia, cable_copia, canalizacion, opcion, interruptor)
            
            if cable_encontrado:
                cables.append(( i+ 1,cable_encontrado))  # Agrega el nuevo cable a la lista
        return cables