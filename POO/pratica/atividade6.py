# Crie um gerador pares.ate(n) que produza números pares de 0 até n (inclusive) usando yield.

def pares_ate(n):
    for i in range(0, n + 1, 2):
        yield i

for par in pares_ate(10):
    print(par)
