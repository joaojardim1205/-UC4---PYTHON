# Enunciado: Crie uma classe Pares que implementa __iter__ e __next__ para iterar apenas números pares de 0 até um limite.

class Pares:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual <= self.limite:
            valor_atual = self.atual
            self.atual += 2
            return valor_atual
        else:
            raise StopIteration

pares = Pares(20)
for numero in pares:
    print(numero)