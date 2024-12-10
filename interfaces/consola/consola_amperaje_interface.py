from core.calculadora_amperaje.calculadora_amperaje_interface import TipoSistema
from core.memoria_calculo import MemoriaDeCalculo


class ConsolaAmperajeInterface:
    def __init__(self   ):
        self.memoria = MemoriaDeCalculo()
    def mostrar_menu(self):
        print("Seleccione el tipo de circuito:")
        for idx, circuito in enumerate( TipoSistema, start=1):
            print(f"{idx}. {circuito.value}")


    def solicitar_datos(self):
        try:
            potencia = float(input("Ingrese la potencia en kW: ")) 
            voltaje = float(input("Ingrese el voltaje en KV: "))
            factor_potencia = float(input("Ingrese el factor de potencia (0-1): "))
            return potencia, voltaje, factor_potencia
        except ValueError:
            print("Entrada no válida. Intente nuevamente.")
            return None, None, None

    def ejecutar(self) :
        self.mostrar_menu()
     
  

