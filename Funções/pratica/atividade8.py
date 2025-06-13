# Enunciado: Crie uma função filtrar pares que recebe uma lista e retorna apenas os números pares. Teste com [1, 2, 3, 4, 5, 6].

def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]

print(filtrar_pares([1, 2, 3, 4, 5, 6]))
