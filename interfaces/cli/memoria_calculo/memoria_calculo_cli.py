# interfaces/cli/calcula_amperaje/calcula_amperaje_cli.py

from application.calculadora_service import CalculadoraService
from domain.entities.carga import Carga
from domain.entities.enums import TipoCarga, TipoSistema
from domain.strategies.calculadora_amperaje_strategy import TrifasicoCalculadora
from domain.strategies.calculo_interruptor_strategy import AlimentadorStrategy




class MemoriaDeCalculoCLI:
    def __init__(self, service: CalculadoraService):
        self.service = service
        self.carga = Carga(
                        nombre="Carga",
                        tipo_circuito= TrifasicoCalculadora(), 
                        tipo_carga=AlimentadorStrategy(), 
                        potencia=0.0, 
                        tension=0.0, 
                        factor_potencia=0.0,
                        hilos=4,
                        longitud=0.0,
                        caida_tension= 3.0)

    
    def menu_inicio_programa(self):
        print("Iniciar Memoria de Calculo:")
        print("1. Calcular Corriente Nominal y ajustes")
        print("2. Seleccionar Interruptor Termomagnetico")
        print("3. Salir")
        return input("Opción: ")
    
    def mostrar_menu_circuito(self):
        print("Seleccione el tipo de circuito:")
        for idx, circuito in enumerate(TipoSistema, start=1):
            print(f"{idx}. {circuito.value}")
        print(f"{len(TipoSistema) + 1}. Salir")
        return input("Opción: ")

    def mostrar_menu_carga(self):
        print("Seleccione el tipo de Carga:")
        for idx, carga in enumerate(TipoCarga, start=1):
            print(f"{idx}. {carga.value}")
        print(f"{len(TipoCarga) + 1}. Salir")
        return input("Opción: ")

    def solicitar_datos_carga(self, tipo_sistema: TipoSistema, tipo_carga: TipoCarga):
        """
        Solicita y configura los datos de la carga del usuario.
        """
        self.carga.tension = float(input("Ingrese el voltaje en V: "))
        self.carga.potencia = float(input("Ingrese la potencia en kW: "))
        self.carga.factor_potencia = float(input("Ingrese el factor de potencia (0-1): "))
        self.carga.tipo_circuito = self.service.tipo_de_sistema_selector(tipo_sistema)
        self.carga.tipo_carga = self.service.tipo_de_carga_selector(tipo_carga)

    def realizar_calculos(self):
        """
        Realiza los cálculos de corriente nominal e interruptor termomagnético.
        """
        print("A)  CALCULO DE LA CORRIENTE NOMINAL")
        self.service.calcular_amperaje(self.carga)
        print(f"Corriente nominal es: {self.carga.corriente_nominal:.2f} A")

        print("B)  CALCULO DEL INTERRUPTOR TERMOMAGNETICO")
        self.service.seleccionar_interruptor(self.carga)
        print(f"Interruptor termomagnético seleccionado: {self.carga.interruptor} A")

    def seleccionar_interruptor_manual(self, tipo_sistema: TipoSistema, tipo_carga: TipoCarga):
        print("B)  SELECCION DEL INTERRUPTOR TERMOMAGNETICO")
        self.carga.interruptor = int(input("Ingrese el interruptor termomagnético en A: "))
        self.carga.tension = float(input("Ingrese el voltaje en V: "))
        self.carga.tipo_circuito = self.service.tipo_de_sistema_selector(tipo_sistema)
        self.carga.tipo_carga = self.service.tipo_de_carga_selector(tipo_carga)
        print(f"Interruptor termomagnético seleccionado: {self.carga.interruptor} A")

    def seleccion_conductor(self, tipo_sistema: TipoSistema):
        print("C)  SELECCION DEL CONDUCTOR")
        print("c.1) Por capacidad de conducción")
        self.service.seleccion_de_cable_por_capacidad_de_conduccion(tipo_sistema)
        print("c.2) Por caída de tensión")
        pass

    def ejecutar(self):
        while True:

            opcion_inicio = self.menu_inicio_programa()
            if opcion_inicio == "3":
                print("Saliendo del programa...")
                break 
            opcion_circuito = self.mostrar_menu_circuito()
            if opcion_circuito == str(len(TipoSistema) + 1):
                break
            opcion_carga = self.mostrar_menu_carga()
            if opcion_carga == str(len(TipoCarga) + 1):
                break
            try:
                tipo_sistema = list(TipoSistema)[int(opcion_circuito) - 1]
                tipo_carga = list(TipoCarga)[int(opcion_carga) - 1]
                if opcion_inicio == "1":

                    self.solicitar_datos_carga(tipo_sistema, tipo_carga)
                    self.realizar_calculos()

                else:
                    self.seleccionar_interruptor_manual(tipo_sistema, tipo_carga)
                    
                    

            except (ValueError, IndexError) as e:
                print(f"Entrada no válida: {e}. Intente nuevamente.")
