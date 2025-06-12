class contador:
    def __init__(self, limite) -> None:
        self.limite = limite
        self.valor = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.valor >= self.limite:
            raise StopIteration
        self.valor += 1
        return self.valor
    
for num in contador(5):
    print(num)