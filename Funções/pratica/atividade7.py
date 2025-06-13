# Enunciado: Crie uma função quadrados que recebe um número n e retorna uma lista com os quadrados de 1 até n. Teste com n = 5.

def quadrados(n):
    return [i**2 for i in range(1, n+1)]

print(quadrados(5))
