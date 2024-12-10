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

    def mostrar_menu_circuito(self):
        print("Seleccione el tipo de circuito:")
        for idx, circuito in enumerate(TipoSistema, start=1):
            print(f"{idx}. {circuito.value}")
        print(f"{len(TipoSistema) + 1}. Salir")

    def mostrar_menu_carga(self):
        print("Seleccione el tipo de Carga:")
        for idx, carga in enumerate(TipoCarga, start=1):
            print(f"{idx}. {carga.value}")
        print(f"{len(TipoCarga) + 1}. Salir")

    def ejecutar(self):
        while True:
            self.mostrar_menu_circuito()
            opcion_circuito = input("Opción: ")
            if opcion_circuito == str(len(TipoSistema) + 1):  # Salir
                print("Saliendo...")
                break
            self.mostrar_menu_carga()
            opcion_carga = input("Opción: ")
            if opcion_carga == str(len(TipoCarga) + 1):
                print("Saliendo...")
                break


            try:
                tipo_sistema = list(TipoSistema)[int(opcion_circuito) - 1]
                tipo_carga = list(TipoCarga)[int(opcion_carga) - 1]
                self.carga.potencia = float(input("Ingrese la potencia en kW: "))
                self.carga.tension = float(input("Ingrese el voltaje en V: "))
                self.carga.factor_potencia = float(input("Ingrese el factor de potencia (0-1): "))
                self.carga.tipo_circuito = self.service.tipo_de_sistema_selector(tipo_sistema)
                self.carga.tipo_carga = self.service.tipo_de_carga_selector(tipo_carga)
                print("A)  CALCULO DE LA CORRIENTE NOMINAL")
                self.service.calcular_amperaje(self.carga)
                print(f"Corriente nominal es: {self.carga.amperaje:.2f} A")
                print("B)  CALCULO DEL INTERRUPTOR TERMOMAGNETICO")
                interruptor = self.service.seleccionar_interruptor(self.carga)
                print(f"Interruptor termomagnético seleccionado: {interruptor} A")
                

            except (ValueError, IndexError):
                print("Entrada no válida. Intente nuevamente.")
