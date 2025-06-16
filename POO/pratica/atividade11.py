# Crie uma classe Circulo com atributo raio e uma propriedade area que calcula a área (π * raio²).

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    @property
    def area(self):
        return math.pi * (self.raio ** 2)

c = Circulo(3)
print(c.area)
