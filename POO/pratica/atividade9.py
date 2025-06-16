# Crie um iterador Fibonacci que gere os primeiros n números da sequência de Fibonacci (1, 1, 2, 3, 5...).

class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.contador = 0
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.n:
            raise StopIteration
        if self.contador == 0 or self.contador == 1:
            self.contador += 1
            return 1
        self.a, self.b = self.b, self.a + self.b
        self.contador += 1
        return self.b

f = Fibonacci(10)
for num in f:
    print(num)
