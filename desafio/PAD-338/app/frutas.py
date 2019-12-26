from abc import ABC

class Frutas(ABC):

    def __init__(self, fruta: str):
        self.fruta = fruta

    def __str__(self):
        return self.fruta

class Banana(Frutas):
    def __init__(self):
        super().__init__('banana')

class Jabuticaba(Frutas):
    def __init__(self):
        super().__init__('jabuticaba')

class Pitanga(Frutas):
    def __init__(self):
        super().__init__('pitanga')

class Mirtilo(Frutas):
    def __init__(self):
        super().__init__('mirtilo')

class Morango(Frutas):
    def __init__(self):
        super().__init__('morango')

class Abacaxi(Frutas):
    def __init__(self):
        super().__init__('abacaxi')

class Cereja(Frutas):
    def __init__(self):
        super().__init__('cereja')


