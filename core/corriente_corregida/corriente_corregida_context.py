from core.corriente_corregida.corriente_corregida_i import CorrienteCorregidaInterface


class ContextoCorrienteCorregida:
    def __init__(self, strategy: CorrienteCorregidaInterface):
        self._strategy = strategy

    def set_strategy(self, strategy: CorrienteCorregidaInterface):
        self._strategy = strategy

    def calcular(self, corriente: float) -> float:
        return self._strategy.calcular(corriente)