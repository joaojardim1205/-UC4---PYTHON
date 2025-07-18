# Enunciado: Tente acessar os primeiros 6 elementos de uma lista com apenas 4 itens. Capture o erro de índice fora do limite.

valores = [1, 2, 3, 4]

for i in range(6):
    try:
        print(f"Elemento na posição {i} é {valores[i]}")
    except IndexError:
        print(f"Não há elemento na posição {i}, a lista só tem {len(valores)} itens.")