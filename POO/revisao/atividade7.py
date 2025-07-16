# Enunciado: Crie uma classe Calculadora com um método soma(a, b) (escopo local) e um método historico() que retorna uma lista de todas as somas realizadas (usando um atributo de classe para armazenar).

class Calculadora:
    def __init__(self):
        self._historico = []

    def soma(self, a, b):
        resultado = a + b
        self._historico.append(resultado)
        return resultado
    
    def historico(self):
        return self._historico
    
calculadora = Calculadora()

print(calculadora.soma(5, 3))
print(calculadora.soma(10, 20))
print(calculadora.historico())