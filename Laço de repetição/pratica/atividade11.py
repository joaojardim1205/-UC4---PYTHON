# Calcule o fatorial de um número usando while.

numero = 15

fatorial = 1
contador = numero

while contador > 1:
    fatorial *= contador
    contador -= 1

print(f"O fatorial de {numero} é {fatorial}.")