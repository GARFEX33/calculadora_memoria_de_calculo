

from core.corriente_corregida.corriente_corregida import TipoCarga
from core.memoria_calculo import MemoriaDeCalculo


class ConsolaMemoriaDeCalculo:
    def __init__(self):
        self.memoria = MemoriaDeCalculo()

    def mostrar_menu(self):
        print("Seleccione el tipo de carga:")
        for idx, carga in enumerate(TipoCarga, start=1):
            print(f"{idx}. {carga.value}")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            try:
                opcion = int(input("Ingrese su opción: "))
                tipo_carga = list(TipoCarga)[opcion - 1]
                self.memoria.seleccionar_tipo_carga(tipo_carga)

                resultado = self.memoria.calcular_amperaje_corregido()
                print(f"La corriente corregida es: {resultado:.2f} A")
            except (IndexError, ValueError) as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nSaliendo...")
                break
