# Enunciado: Crie uma classe Forma com um método area() que retorna 0. Em seguida, crie as classes Quadrado e Circulo que herdam de Forma e sobrescrevem area() para calcular suas respectivas áreas. Use polimorfismo para chamar o método area() de cada objeto.

class Forma:
    def area(self):
        return 0
    
class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        import math
        return math.pi * (self.raio ** 2)
    
# Enunciado: Crie uma função imprimir_area() que recebe um objeto do tipo Forma (da atividade anterior) e imprime sua área. Demonstre o polimorfismo passando objetos de Quadrado e Circulo.
 
def imprimir_area(forma):
    print(f"A área é: {forma.area()}")

quadrado = Quadrado(4)
circulo = Circulo(3)

imprimir_area(quadrado) 
imprimir_area(circulo)