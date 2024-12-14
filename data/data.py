from typing import List, Tuple


class DataList:
    
    def get_lista_de_interruptores(self) -> List[Tuple[int, int]]:
        interruptores = [
                        (10, 1),
                        (15, 1),
                        (20, 1),
                        (30, 1),
                        (40, 1),
                        (50, 1),
                        (60, 1),
                        (70, 1),
                        (80, 1),
                        (90, 1),
                        (100, 1),
                        (125, 1),
                        (150, 1),
                        (175, 1),
                        (200, 1),
                        (225, 1),
                        (250, 1),
                        (300, 2),
                        (400, 2),
                        (500, 2),
                        (600, 2),
                        (700, 3),
                        (800, 3),
                        (1000, 4),
                        (1200, 4),
                        (1600, 4),
                        (2000, 6),
                        (2500, 6),
                        (3200, 6),
                        (4000, 6),
                        (5000, 6),
                        (6300, 6)
                    ]
        return interruptores

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
    
    def get_factorTemperatura60A30C(self) -> List[Tuple[int, int, float]]: 
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
    
    def get_factorTemperatura75A30C(self) -> List[Tuple[int, int, float]]:
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

    def get_ampacidadCobreTemp90Tubo(self) -> List[Tuple[str, int]]:
        ampacidad90CTubo = [
                            ("14", 25),
                            ("12", 30),
                            ("10", 40),
                            ("8", 55),
                            ("6", 75),
                            ("4", 95),
                            ("2", 130),
                            ("1/0", 170),
                            ("2/0", 195),
                            ("3/0", 225),
                            ("4/0", 260),
                            ("250", 290),
                            ("300", 320),
                            ("350", 350),
                            ("400", 380),
                            ("500", 430),
                            ("600", 475),
                            ("750", 535),
                            ("1000", 615)
                        ]

        return ampacidad90CTubo

    def get_ampacidadAluminioTemp60Tubo(self) -> List[Tuple[str, int]]:
        ampacidad60AluminioTubo = [
                                    ("6", 40),
                                    ("4", 55),
                                    ("2", 75),
                                    ("1/0", 100),
                                    ("2/0", 115),
                                    ("3/0", 130),
                                    ("4/0", 150),
                                    ("250", 170),
                                    ("300", 195),
                                    ("350", 210),
                                    ("400", 225),
                                    ("500", 260),
                                    ("600", 285),
                                    ("750", 320),
                                    ("1000", 375)
                                ]

        return ampacidad60AluminioTubo

    def get_ampacidadAluminioTemp75Tubo(self) -> List[Tuple[str, int]]:
        ampacidad75AluminioTubo = [
                                    ("6", 50),
                                    ("4", 65),
                                    ("2", 90),
                                    ("1/0", 120),
                                    ("2/0", 135),
                                    ("3/0", 155),
                                    ("4/0", 180),
                                    ("250", 205),
                                    ("300", 230),
                                    ("350", 250),
                                    ("400", 270),
                                    ("500", 310),
                                    ("600", 340),
                                    ("750", 385),
                                    ("1000", 445)
                                ]
        return ampacidad75AluminioTubo

    def get_ampacidadAluminioTemp90Tubo(self) -> List[Tuple[str, int]]:
        ampacidad90AluminioTubo = [
                        ("6", 55),
                        ("4", 75),
                        ("2", 100),
                        ("1/0", 135),
                        ("2/0", 150),
                        ("3/0", 175),
                        ("4/0", 205),
                        ("250", 230),
                        ("300", 260),
                        ("350", 280),
                        ("400", 305),
                        ("500", 350),
                        ("600", 385),
                        ("750", 435),
                        ("1000", 500)
                    ]

        return ampacidad90AluminioTubo

    def get_ampacidadCobreTemp60Charola(self) -> List[Tuple[str, int]]:
        ampacidad60CCharola = [
                            ("14", 25),
                            ("12", 30),
                            ("10", 40),
                            ("8", 60),
                            ("6", 80),
                            ("4", 105),
                            ("2", 140),
                            ("1/0", 195),
                            ("2/0", 225),
                            ("3/0", 260),
                            ("4/0", 300),
                            ("250", 340),
                            ("300", 375),
                            ("350", 420),
                            ("400", 455),
                            ("500", 515),
                            ("600", 575),
                            ("750", 655),
                            ("1000", 780)
                        ]
        return ampacidad60CCharola

    def get_ampacidadCobreTemp75Charola(self) -> List[Tuple[str, int]]:
        ampacidad75CCharola = [
                            ("14", 30),
                            ("12", 35),
                            ("10", 50),
                            ("8", 70),
                            ("6", 95),
                            ("4", 125),
                            ("2", 170),
                            ("1/0", 230),
                            ("2/0", 265),
                            ("3/0", 310),
                            ("4/0", 360),
                            ("250", 405),
                            ("300", 445),
                            ("350", 505),
                            ("400", 545),
                            ("500", 620),
                            ("600", 690),
                            ("750", 785),
                            ("1000", 935)
                        ]
        return ampacidad75CCharola
    
    def get_ampacidadCobreTemp90Charola(self) -> List[Tuple[str, int]]:
        ampacidad90CCharola = [
                            ("14", 35),
                            ("12", 40),
                            ("10", 55),
                            ("8", 80),
                            ("6", 105),
                            ("4", 140),
                            ("2", 190),
                            ("1/0", 260),
                            ("2/0", 300),
                            ("3/0", 350),
                            ("4/0", 405),
                            ("250", 455),
                            ("300", 500),
                            ("350", 570),
                            ("400", 615),
                            ("500", 700),
                            ("600", 780),
                            ("750", 885),
                            ("1000", 1055)
                        ]
        return ampacidad90CCharola

    def get_ampacidadAluminioTemp60Charola(self) -> List[Tuple[str, int]]:
        ampacidad = [
                            ("6", 60),
                            ("4", 80),
                            ("2", 110),
                            ("1/0", 150),
                            ("2/0", 175),
                            ("3/0", 200),
                            ("4/0", 235),
                            ("250", 265),
                            ("300", 290),
                            ("350", 330),
                            ("400", 355),
                            ("500", 405),
                            ("600", 455),
                            ("750", 515),
                            ("1000", 625)
                                        ]

        return ampacidad

    def get_ampacidadAluminioTemp75Charola(self) -> List[Tuple[str, int]]:
        ampacidad = [
                            ("6", 75),
                            ("4", 100),
                            ("2", 135),
                            ("1/0", 180),
                            ("2/0", 210),
                            ("3/0", 240),
                            ("4/0", 280),
                            ("250", 315),
                            ("300", 350),
                            ("350", 395),
                            ("400", 425),
                            ("500", 485),
                            ("600", 545),
                            ("750", 620),
                            ("1000", 750)
                        ]
        return ampacidad

    def get_ampacidadAluminioTemp90Charola(self) -> List[Tuple[str, int]]:
        ampacidad = [
                        ("6", 85),
                        ("4", 115),
                        ("2", 150),
                        ("1/0", 205),
                        ("2/0", 235),
                        ("3/0", 270),
                        ("4/0", 315),
                        ("250", 355),
                        ("300", 395),
                        ("350", 445),
                        ("400", 480),
                        ("500", 545),
                        ("600", 615),
                        ("750", 700),
                        ("1000", 845)
                    ]
        return ampacidad
    
    def get_ampacidad_cobre_75C_a_40C_charola_triangular(self):
        ampacidad = [
                        ("8", 57),
                        ("6", 76),
                        ("4", 101),
                        ("2", 118),
                        ("1/0", 183),
                        ("2/0", 212),
                        ("3/0", 245),
                        ("4/0", 287),
                        ("250", 320),
                        ("300", 359),
                        ("350", 397),
                        ("400", 430),
                        ("500", 496),
                        ("600", 553),
                        ("750", 638),
                        ("1000", 748)
                    ]
        return ampacidad

    def get_ampacidad_cobre_90C_a_40C_charola_triangular(self):
        ampacidad = [
                        ("8", 66),
                        ("6", 89),
                        ("4", 117),
                        ("2", 138),
                        ("1/0", 214),
                        ("2/0", 247),
                        ("3/0", 287),
                        ("4/0", 335),
                        ("250", 374),
                        ("300", 419),
                        ("350", 464),
                        ("400", 503),
                        ("500", 580),
                        ("600", 647),
                        ("750", 747),
                        ("1000", 879)
                    ]
        return ampacidad

    def get_ampacidad_aluminio_75C_a_40C_charola_triangular(self):
        ampacidad = [
                        ("6", 59),
                        ("4", 78),
                        ("2", 92),
                        ("1/0", 143),
                        ("2/0", 165),
                        ("3/0", 192),
                        ("4/0", 224),
                        ("250", 251),
                        ("300", 282),
                        ("350", 312),
                        ("400", 339),
                        ("500", 392),
                        ("600", 440),
                        ("750", 512),
                        ("1000", 612)
                    ]
        return ampacidad
    
    def get_ampacidad_aluminio_90C_a_40C_charola_triangular(self):
        ampacidad = [
                        ("6", 69),
                        ("4", 91),
                        ("2", 107),
                        ("1/0", 167),
                        ("2/0", 193),
                        ("3/0", 224),
                        ("4/0", 262),
                        ("250", 292),
                        ("300", 328),
                        ("350", 364),
                        ("400", 395),
                        ("500", 458),
                        ("600", 514),
                        ("750", 598),
                        ("1000", 716)
                    ]
        return ampacidad
