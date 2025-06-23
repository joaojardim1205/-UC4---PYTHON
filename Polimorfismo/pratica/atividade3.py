# Crie uma classe Ponto com coordenadasey, Sobrescreva o método add para que dois pontos possam ser somados.

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Ponto(2, 3)
p2 = Ponto(4, 5)
p3 = p1 + p2

print(p3)
