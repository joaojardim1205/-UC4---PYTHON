# Crie uma classe Calculadora com um atributo de classe operacoes quantas operações foram feitas

class Calculadora:
    operacoes = 0

    def somar(self, a, b):
        Calculadora.operacoes += 1
        return a + b

    def subtrair(self, a, b):
        Calculadora.operacoes += 1
        return a - b

    def multiplicar(self, a, b):
        Calculadora.operacoes += 1
        return a * b

    def dividir(self, a, b):
        Calculadora.operacoes += 1
        return a / b

calc = Calculadora()
print(calc.somar(3, 4))
print(calc.subtrair(10, 5))
print(Calculadora.operacoes)
