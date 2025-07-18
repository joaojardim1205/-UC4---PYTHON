# Enunciado: Tente acessar uma chave em um dicionário que pode não existir. Use try e except para capturar o erro ao acessar uma chave ausente.

dicionario = {'a': 1, 'b': 2, 'c': 3}
chaves = ['a', 'b', 'd', 'e']

for chave in chaves:
    try:
        valor = dicionario[chave]
        print(f"O valor associado à chave '{chave}' é {valor}")
    except KeyError:
        print(f"A chave '{chave}' não existe no dicionário.")