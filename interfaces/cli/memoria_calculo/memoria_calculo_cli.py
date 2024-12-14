# interfaces/cli/calcula_amperaje/calcula_amperaje_cli.py

from application.calculadora_service import CalculadoraService
from domain.entities.cable import Cable
from domain.entities.carga import Carga
from domain.entities.enums import Canalizacion, TipoCarga, TipoMaterialCable, TipoSistema


class MemoriaDeCalculoCLI:
    def __init__(self, service: CalculadoraService):
        self.service = service
        self.canalizacion: Canalizacion 
        self.cable: Cable = Cable()
        self.carga: Carga 
        self.tipo_circuito: TipoSistema = TipoSistema.ESTRELLA
        self.tipo_carga: TipoCarga = TipoCarga.ALIMENTADOR
    
    def menu_inicio_programa(self):
        print("\nIniciar Memoria de Calculo:\n")
        print("1. Calcular Corriente Nominal y ajustes")
        print("2. Seleccionar Interruptor Termomagnetico")
        print("3. Salir")
        return input("Opción: ")

    def menu_circuito(self) -> bool:
        print("Seleccione el tipo de circuito:")
        for idx, circuito in enumerate(TipoSistema, start=1):
            print(f"{idx}. {circuito.value}")
        print(f"{len(TipoSistema) + 1}. Salir")
        opcion = input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(TipoSistema):
            self.circuito = list(TipoSistema)[int(opcion) - 1]
            return False
        elif opcion == str(len(TipoSistema) + 1):
            print("Saliendo del menú...")
            return True
        else:
            print("Opción inválida. Intente de nuevo.")
            return self.menu_circuito()

    def menu_tipo_carga(self) -> bool:
        print("Seleccione el tipo de Carga:")
        for idx, carga in enumerate(TipoCarga, start=1):
            print(f"{idx}. {carga.value}")
        print(f"{len(TipoCarga) + 1}. Salir")
        opcion =  input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(TipoCarga):
            self.tipo_carga = list(TipoCarga)[int(opcion) - 1]
            return False
        elif opcion == str(len(TipoCarga) + 1):
            print("Saliendo del menú...")
            return True
        else:
            print("Opción inválida. Intente de nuevo.")
            return self.menu_tipo_carga()
        
    def menu_seleccion_tipo_material_conductor(self) -> bool:
        print("Seleccione el tipo de material del conductor:")
        for idx, material in enumerate(TipoMaterialCable, start=1):
            print(f"{idx}. {material.value}")
        print(f"{len(TipoMaterialCable) + 1}. Salir")
        opcion = input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(TipoMaterialCable):
            self.cable.material = list(TipoMaterialCable)[int(opcion) - 1]
            return False
        elif opcion == str(len(TipoMaterialCable) + 1):
            print("Saliendo del menú...")
            return True
        else:
            print("Opción inválida. Intente de nuevo.")
            return self.menu_seleccion_tipo_material_conductor()

    def menu_seleccion_canalizacion(self) -> bool:
        print("Seleccione el tipo de canalización:")
        for idx, canalizacion in enumerate(Canalizacion, start=1):
            print(f"{idx}. {canalizacion.value}")
        print(f"{len(Canalizacion) + 1}. Salir")
        
        opcion = input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(Canalizacion):
            self.canalizacion = list(Canalizacion)[int(opcion) - 1]
            return False
        elif opcion == str(len(Canalizacion) + 1):
            print("Saliendo del menú...")
            return True
        else:
            print("Opción inválida. Intente de nuevo.")
            return self.menu_seleccion_canalizacion()

    def solicitar_datos_carga(self):

        self.carga = Carga(
            tipo_circuito = self.tipo_circuito,
            tipo_carga = self.tipo_carga,
             )
        self.carga.tension = float(input("Ingrese el voltaje en V: "))
        self.carga.potencia = float(input("Ingrese la potencia en kW: "))
        self.carga.factor_potencia = float(input("Ingrese el factor de potencia (0-1): "))

    def realizar_calculos(self):

        print("A)  CALCULO DE LA CORRIENTE NOMINAL")
        self.service.calcular_amperaje(self.carga)
        print(f"Corriente nominal es: {self.carga.corriente_nominal:.2f} A")

        print("B)  CALCULO DEL INTERRUPTOR TERMOMAGNETICO")
        self.service.seleccionar_interruptor(self.carga)
        print(f"Interruptor termomagnético seleccionado: {self.carga.interruptor} A")

    def seleccionar_interruptor_manual(self):
        print("B)  SELECCION DEL INTERRUPTOR TERMOMAGNETICO")
        self.carga.interruptor = int(input("Ingrese el interruptor termomagnético en A: "))
        self.carga.tension = float(input("Ingrese el voltaje en V: "))
        self.carga.corriente_nominal = self.carga.interruptor
        print(f"Interruptor termomagnético seleccionado: {self.carga.interruptor} A")

    def seleccion_conductor(self,opcion: str):

        print("C)  SELECCION DEL CONDUCTOR")
        print("c.1) Por capacidad de conducción")
        self.cable.seleccionar_temperatura_cable(self.carga.capacidad_conduccion)
        self.carga.capacidad_conduccion = self.service.seleccion_de_cable_por_capacidad_de_conduccion( self.tipo_circuito ,self.carga, self.cable, opcion)
        print(f"Corriente por capacidad de conduccion es: {self.carga.capacidad_conduccion :.2f}")
        self.cable.calibre, self.cable.amperaje = self.service.selecionar_cable(self.carga,self.cable,self.canalizacion , self.tipo_circuito, opcion)
        print(f"Calibre seleccionado: {self.cable.calibre} en {self.cable.material.value} con ampacidad de {self.cable.amperaje} A, en canalizacion de {self.canalizacion.value}")
        
        print("c.2) Por caída de tensión")
        pass

    def ejecutar(self):
        while True:

            opcion_inicio = self.menu_inicio_programa()
            if opcion_inicio == "3":
                print("Saliendo del programa...")
                break 
            if self.menu_circuito():
                break

            if self.menu_tipo_carga():
                break
            if self.menu_seleccion_tipo_material_conductor():
                break

            if self.menu_seleccion_canalizacion():
                break

            try:
     
                if opcion_inicio == "1":
                    self.solicitar_datos_carga()
                    self.realizar_calculos()
                    self.seleccion_conductor(opcion_inicio)
                    print("Memoria de cálculo finalizada.")
                    #break
                else:
                    self.seleccionar_interruptor_manual()
                    self.seleccion_conductor(opcion_inicio)
                    print("Memoria de cálculo finalizada.")
                    #break

            except (ValueError, IndexError) as e:
                print(f"Entrada no válida: {e}. Intente nuevamente.")
