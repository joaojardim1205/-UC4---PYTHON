# Enunciado: Crie uma classe Contador que implementa o protocolo de iterador (com __iter__ e__next__). O iterador deve contar de 0 até um limite definido no construtor, incrementando de 1 em 1.

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.atual < self.limite:
            valor_atual = self.atual
            self.atual += 1
            return valor_atual
        else:
            raise StopIteration