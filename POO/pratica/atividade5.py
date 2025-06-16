# Crie um iterador Contador Regressivo que receba um número inicial e conte regressivamente até 0. Use iter()e next().

class ContadorRegressivo:
    def __init__(self, inicio):
        self.atual = inicio

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < 0:
            raise StopIteration
        valor = self.atual
        self.atual -= 1
        return valor

contador = ContadorRegressivo(5)
iterador = iter(contador)

for numero in iterador:
    print(numero)
