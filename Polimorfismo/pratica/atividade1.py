# Crie très classes (Circulo, Quadrado, Triangulo) que implementam um método calcular_area().
# Depois, crie uma função imprimir aree(forma) que recebe qualquer uma dessas formas e imprime sua área

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def imprimir_area(forma):
    print(f"A área é: {forma.calcular_area():.2f}")

c = Circulo(5)
q = Quadrado(4)
t = Triangulo(6, 3)

imprimir_area(c)  
imprimir_area(q)
imprimir_area(t) 