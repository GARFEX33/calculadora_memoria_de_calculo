from typing import List, Tuple


class DataList:
    
    def get_factorAgrupamiento(self) -> List[Tuple[int, int, float]]:
        factorAgrupamiento = [
            (1, 3, 1.0),
            (4, 6, 0.8),
            (7, 9, 0.7),
            (10, 20, 0.5),
            (21, 30, 0.45),
            (31, 40, 0.4),
            (41, 100, 0.35) 
        ]
        return factorAgrupamiento
    
    def get_FactorTemperatura60A30C(self) -> List[Tuple[int, int, float]]: 
        FactorTemperatura60A30C = [
            (1, 10, 1.29),
            (11, 15, 1.22),
            (16, 20, 1.15),
            (21, 25, 1.08),
            (26, 30, 1.0),
            (31, 35, 0.91),
            (36, 40, 0.82),
            (41, 45, 0.71),
            (46, 50, 0.58),
            (51, 55, 0.41)
        ]
        return FactorTemperatura60A30C
    
    def get_FactorTemperatura75A30C(self) -> List[Tuple[int, int, float]]:
        FactorTemperatura75A30C = [
            (1, 10, 1.2),
            (11, 15, 1.15),
            (16, 20, 1.11),
            (21, 25, 1.05),
            (26, 30, 1.0),
            (31, 35, 0.94),
            (36, 40, 0.88),
            (41, 45, 0.82),
            (46, 50, 0.75),
            (51, 55, 0.67),
            (56, 60, 0.58),
            (61, 65, 0.47)
        ]
        return FactorTemperatura75A30C
    
    def get_ampacidadCobreTemp60Tubo(self) -> List[Tuple[str, int]]:
        ampacidad60CTubo = [
        ("14", 15),
        ("12", 20),
        ("10", 30),
        ("8", 40),
        ("6", 55),
        ("4", 70),
        ("3", 85),
        ("2", 95),
        ("1", 110),
        ]
        return ampacidad60CTubo
    
    def get_ampacidadCobreTemp75Tubo(self) -> List[Tuple[str, int]]:
        ampacidad75CTubo = [
                            ("14", 20),
                            ("12", 25),
                            ("10", 35),
                            ("8", 50),
                            ("6", 65),
                            ("4", 85),
                            ("2", 115),
                            ("1/0", 150),
                            ("2/0", 175),
                            ("3/0", 200),
                            ("4/0", 230),
                            ("250", 255),
                            ("300", 285),
                            ("350", 310),
                            ("400", 335),
                            ("500", 380),
                            ("600", 420),
                            ("750", 475),
                            ("1000", 545)
                                            ]
        return ampacidad75CTubo