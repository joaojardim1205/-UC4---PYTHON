# Crie um gerador primos_ate(n) que produza todos os números primos até n.

def primos_ate(n):
    for num in range(2, n + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

for primo in primos_ate(30):
    print(primo)
