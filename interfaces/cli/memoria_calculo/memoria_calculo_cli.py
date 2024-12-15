# interfaces/cli/calcula_amperaje/calcula_amperaje_cli.py

from application.calculadora_service import CalculadoraService
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoCarga, TipoCircuito
from domain.entities.interruptor import *
from interfaces.cli.memoria_calculo.menu_memoria_calculo_cli import MenuMemoriaDeCalculoCli


class MemoriaDeCalculoCLI:
    def __init__(self, service: CalculadoraService):
        self.service = service
        self.canalizacion: Canalizacion | None = None
        self.cable: Cable = Cable()
        self.carga: Carga 
        self.menu: MenuMemoriaDeCalculoCli = MenuMemoriaDeCalculoCli(self.cable)
        self.tipo_circuito: TipoCircuito  | None = None
        self.tipo_carga: TipoCarga | None = None
        self.interruptor: Interruptor = Interruptor()
        
    
    def solicitar_datos_carga(self):
        if self.tipo_circuito and  self.tipo_carga is not None:
            self.carga = Carga(
                tipo_circuito = self.tipo_circuito,
                tipo_carga = self.tipo_carga,
                )
        self.carga.tension = float(input("Ingrese el voltaje en V: "))
        self.carga.potencia = float(input("Ingrese la potencia en kW: "))
        self.carga.factor_potencia = float(input("Ingrese el factor de potencia (0-1): "))

    def realizar_calculo_corriente_nominal(self):

        print("A)  CALCULO DE LA CORRIENTE NOMINAL")
        self.service.calcular_amperaje(self.carga)
        print(f"Corriente nominal: {self.carga.corriente_nominal:.2f} A")

    def calculo_del_interruptor_termomagnetico(self):
        print("B)  CALCULO DEL INTERRUPTOR TERMOMAGNETICO")
        self.service.seleccionar_interruptor(self.carga, self.interruptor)
        if self.tipo_circuito is not None:
            print(f"Interruptor termomagnético seleccionado: {self.service.seleccionar_numero_hilos_interruptor(self.tipo_circuito)}X{self.interruptor.ampacidad}A")
        else:
            print("Error: Tipo de circuito no seleccionado.")

    def seleccionar_interruptor_manual(self):
        if self.tipo_circuito and  self.tipo_carga is not None:
            self.carga = Carga(
                tipo_circuito = self.tipo_circuito,
                tipo_carga = self.tipo_carga,
                )
        print("B)  SELECCION DEL INTERRUPTOR TERMOMAGNETICO")
        self.carga.tension = float(input("Ingrese el voltaje en V: "))
        self.interruptor.ampacidad = int(input("Ingrese el interruptor termomagnético en A: "))
        self.carga.corriente_nominal = self.interruptor.ampacidad
        print("Tipo de carga:", self.carga.tipo_carga)
        self.interruptor.seleccionar_interruptor(self.carga.corriente_nominal)
  
        if self.tipo_circuito is not None:
            print(f"Interruptor termomagnético seleccionado: {self.service.seleccionar_numero_hilos_interruptor(self.tipo_circuito)}X{self.interruptor.ampacidad} A")
        else:
            print("Error: Tipo de circuito no seleccionado.")

    def seleccion_conductor(self,opcion: str):

        print("C)  SELECCION DEL CONDUCTOR")
        print("c.1) Por capacidad de conducción")
        self.cable.seleccionar_temperatura_cable(self.carga.capacidad_conduccion)
        if self.tipo_circuito and self.canalizacion is not None:
            self.carga.capacidad_conduccion = self.service.seleccion_de_cable_por_capacidad_de_conduccion(  self.carga, self.cable, opcion)
            print(f"Corriente por capacidad de conduccion es: {self.carga.capacidad_conduccion :.2f}")
            lista_cables = self.service.lista_de_cables_seleccionados(self.carga, self.interruptor, self.cable, self.canalizacion, opcion)
            print(lista_cables)
            for numero_fases, cable in lista_cables:
                print(f"Cable seleccionado {numero_fases}-{cable.calibre}THHN de {cable.material.value} soporta {cable.amperaje}A")
        print("c.2) Por caída de tensión")
        pass

    def ejecutar(self):
        while True:

            opcion_inicio = self.menu.menu_inicio_programa()
            if opcion_inicio == "3":
                print("Saliendo del programa...")
                break 
            self.tipo_circuito = self.menu.menu_circuito()
            if self.tipo_circuito == None:
                break
            self.tipo_carga = self.menu.menu_tipo_carga()
            if self.tipo_carga  == None:
                break
            if self.menu.menu_seleccion_tipo_material_conductor():
                break
            self.canalizacion = self.menu.menu_seleccion_canalizacion()
            if self.canalizacion == None:
                break

            try:
     
                if opcion_inicio == "1":
                    self.solicitar_datos_carga()
                    self.realizar_calculo_corriente_nominal()
                    self.interruptor.calcular_tipo_carga = self.service.seleccionar_tipo_de_carga(self.carga)
                    self.calculo_del_interruptor_termomagnetico()
                    self.seleccion_conductor(opcion_inicio)
                    print("Memoria de cálculo finalizada.")
                    #break
                else:
                    self.seleccionar_interruptor_manual()
                    self.interruptor.calcular_tipo_carga = self.service.seleccionar_tipo_de_carga(self.carga)

                    self.seleccion_conductor(opcion_inicio)
                    print("Memoria de cálculo finalizada.")
                    #break

            except (ValueError, IndexError) as e:
                print(f"Entrada no válida: {e}. Intente nuevamente.")
