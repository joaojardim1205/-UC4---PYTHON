# Crie um módulo fatorial.py com uma função recursiva calcular_fatorial(n) que retorne o fatorial de um número.

def calcular_fatorial(n):
    if n < 0:
        raise ValueError("O fatorial não está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)