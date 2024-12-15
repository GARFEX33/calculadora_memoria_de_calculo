from domain.entities.cable import Cable
from domain.entities.enums import Canalizacion, TipoCarga, TipoMaterialCable, TipoCircuito
class MenuMemoriaDeCalculoCli:
    def __init__(self, cable: Cable):
        self.cable: Cable = cable

    def menu_inicio_programa(self) -> str:
        print("\nIniciar Memoria de Calculo:\n")
        print("1. Calcular Corriente Nominal y ajustes")
        print("2. Seleccionar Interruptor Termomagnetico")
        print("3. Salir")
        return input("Opción: ")

    def menu_circuito(self) -> TipoCircuito | None:
        print("Seleccione el tipo de circuito:")
        for idx, circuito in enumerate(TipoCircuito, start=1):
            print(f"{idx}. {circuito.value}")
        print(f"{len(TipoCircuito) + 1}. Salir")
        opcion = input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(TipoCircuito):
            return list(TipoCircuito)[int(opcion) - 1]
        elif opcion == str(len(TipoCircuito) + 1):
            print("Saliendo del menú...")
            return None
        else:
            print("Opción inválida. Intente de nuevo.")
            return self.menu_circuito()

    def menu_tipo_carga(self) -> TipoCarga | None:
        print("Seleccione el tipo de Carga:")
        for idx, carga in enumerate(TipoCarga, start=1):
            print(f"{idx}. {carga.value}")
        print(f"{len(TipoCarga) + 1}. Salir")
        opcion =  input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(TipoCarga):
            return list(TipoCarga)[int(opcion) - 1]
        elif opcion == str(len(TipoCarga) + 1):
            print("Saliendo del menú...")
            return None
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

    def menu_seleccion_canalizacion(self) -> Canalizacion | None:
        print("Seleccione el tipo de canalización:")
        for idx, canalizacion in enumerate(Canalizacion, start=1):
            print(f"{idx}. {canalizacion.value}")
        print(f"{len(Canalizacion) + 1}. Salir")
        
        opcion = input("Opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(Canalizacion):
            return list(Canalizacion)[int(opcion) - 1]
        elif opcion == str(len(Canalizacion) + 1):
            print("Saliendo del menú...")
            return None
        else:
            print("Opción inválida. Intente de nuevo.")
            return self.menu_seleccion_canalizacion()
