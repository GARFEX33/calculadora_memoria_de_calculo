from copy import deepcopy
from typing import TYPE_CHECKING, List
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoCarga, TipoCircuito

from domain.entities.interruptor import Interruptor
from domain.entities.lista_cables import CableSelecciondo
from domain.strategies.calculo_interruptor_strategy import AlimentadorStrategy, CalculoDeInterruptorStrategy, FiltroStrategy, MotorStrategy, SeleccionInterruptor
from domain.strategies.seleccion_conduccion_strategy import  SeleccionConduccionTrifasicaITMStrategy, SeleccionConduccionTrifasicaStrategy
from domain.strategies.seleccionar_seccion_cable_strategy import SeleccionarSeccionDeCable

if TYPE_CHECKING:
    from interfaces.desktop.main import CalculadoraGARFEX
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
    
    def seleccion_de_cable_por_capacidad_de_conduccion(self, app: "CalculadoraGARFEX") -> float:
       
        if app.carga.tipo_circuito == TipoCircuito.ESTRELLA and app.opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(app.cable, app.carga)
        elif app.carga.tipo_circuito == TipoCircuito.ESTRELLA and app.opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(app.cable, app.carga)
        elif app.carga.tipo_circuito == TipoCircuito.DELTA and app.opcion == "1":
            return SeleccionConduccionTrifasicaStrategy().capacidad_de_conduccion(app.cable, app.carga)
        elif app.carga.tipo_circuito == TipoCircuito.DELTA and app.opcion == "2":
            return SeleccionConduccionTrifasicaITMStrategy().capacidad_de_conduccion(app.cable, app.carga)
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
    
    def lista_de_cables_seleccionados(self,app: "CalculadoraGARFEX")-> List[ CableSelecciondo ]:
        cables: List[ CableSelecciondo]= []
        for i in range(app.interruptor.bornes):
            carga_copia = deepcopy(app.carga)
            carga_copia.capacidad_conduccion = app.carga.capacidad_conduccion / (i + 1)
            cable_copia = deepcopy(app.cable)
            cable_encontrado = self.selecionar_cable(carga_copia, cable_copia, app.canalizacion, app.opcion, app.interruptor)
            if cable_encontrado:  
                cable_seleccionado = CableSelecciondo(
                    cable= cable_encontrado,
                    cable_por_fase= i + 1,
                    #total_costo= cable_encontrado.costo * (i + 1)
                )
                            
                cables.append(cable_seleccionado) 
        return cables
    
    def seleccionar_temperatura_cable(self, app: "CalculadoraGARFEX"):
        if app.carga.corriente_nominal < 100:
            app.cable.temperatura = 60
        else: 
            app.cable.temperatura = 75
    
    def calcular_numero_hilos_carga(self, app: "CalculadoraGARFEX"):
        if app.carga.tipo_circuito == TipoCircuito.ESTRELLA:
            app.carga.hilos = 4
        elif app.carga.tipo_circuito == TipoCircuito.DELTA:
            app.carga.hilos = 3
        else:
            raise ValueError("Tipo de sistema no válido")
        
    def calcular_caida_de_tension(self, app: "CalculadoraGARFEX"):
            return app.carga.calcular_caida_de_tension(app)

    def seleccionar_seccion_cable(self, cable: Cable):
        return SeleccionarSeccionDeCable(cable).seleccionar()