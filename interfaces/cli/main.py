# interfaces/cli/main.py
from application.calculadora_service import CalculadoraService
from interfaces.cli.memoria_calculo.memoria_calculo_cli import MemoriaDeCalculoCLI


def main():
    cli_amperaje = MemoriaDeCalculoCLI(CalculadoraService())
    cli_amperaje.ejecutar()


if __name__ == "__main__":
    main()
