def gerador_pares(limite):
    for num in range(limite):
        if num % 2 == 0:
            yield num

for par in gerador_pares(10):
    print(par)

    