# Enunciado: Dada a lista [1, 6, 2, 8, 3, 91, use filter() e uma lambda para retornar apenas números maiores que 5.

lista = [1, 6, 2, 8, 3, 91]

resultado = list(filter(lambda x: x > 5, lista))

print(resultado)
