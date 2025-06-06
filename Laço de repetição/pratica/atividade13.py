# Use for para verificar se uma palavra é um palíndromo (lê-se igual de trás para frente).

palavra = 'arara'
palindromo = True
tamanho = len(palavra)

for i in range(tamanho // 2):
    if palavra[i] != palavra[tamanho - 1 - i]:
        palindromo = False
        break

if palindromo:
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')