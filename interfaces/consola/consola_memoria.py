from core.memoria_calculo import MemoriaDeCalculo
from ui.consola.consola_amperaje_interface import ConsolaAmperajeInterface


class ConsolaMemoria:
    def __init__(self, memoria: MemoriaDeCalculo ):
        self.amperaje = 0
        self.memoria = memoria
        self.consola_amperaje = ConsolaAmperajeInterface(self.memoria.amperaje)


    def mostrar_menu(self) -> None:
        print("Seleccione Si desea calcular amperaje o solo ingresarlo:")
        print("1. Calcular amperaje")
        print("2. Ingresar amperaje")

    def obtener_opcion(self):
        try:
            opcion = int(input("Ingrese su opción (1 o 2): "))
            if opcion not in (1, 2):
                raise ValueError("Opción inválida")
            return opcion
        except ValueError as e:
            print(e)
            return None
    
    def ejecutar(self):
        self.mostrar_menu()
        opcion = self.obtener_opcion()
        if not opcion:
            return
        
        if opcion == 1:
            self.amperaje = self.consola_amperaje.ejecutar()
            print(f"El amperaje Calculado es: {self.amperaje:.2f} A")

        elif opcion == 2:
            self.amperaje = self.memoria.ingresar_amperaje()
            print(f"El amperaje ingresado es: {self.amperaje:.2f} A")
        else:
            print("Opción inválida")
            return