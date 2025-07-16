# Em seguida, no main.py, importe a função e teste com alguns números.

from validacao import eh_par

numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    if eh_par(numero):
        print(f"{numero} é par.")
    else:
        print(f"{numero} é ímpar.")