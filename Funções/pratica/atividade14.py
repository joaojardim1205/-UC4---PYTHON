# Enunciado: Ordene a lista | ("João", 25), ("Maria", 30), ("Carlos", 20)] pela idade usando sorted() e uma lambda.

lista = [("João", 25), ("Maria", 30), ("Carlos", 20)]

ordenada = sorted(lista, key=lambda x: x[1])

print(ordenada)
