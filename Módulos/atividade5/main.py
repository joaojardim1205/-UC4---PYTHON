# No main.py, importe e teste a função.

from fatorial import calcular_fatorial

def teste():
        numero = 10
        resultado = calcular_fatorial(numero)
        print(f"O fatorial de {numero} é {resultado}.")
teste()