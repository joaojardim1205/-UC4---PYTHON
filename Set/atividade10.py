# Enunciado: Crie dois conjuntos:
# ● todos_os_numeros com {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# ● numeros_pares com {2, 4, 6, 8, 10}
# Encontre e imprima os números que estão no primeiro conjunto mas não estão no segundo (os números ímpares).

todos_os_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numeros_pares = {2, 4, 6, 8, 10}
numeros_impares = todos_os_numeros - numeros_pares
print(numeros_impares)
