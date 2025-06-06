# Use for para contar quantas vezes a letra "a" aparece em uma palavra.

palavra = 'batata'
contador = 0

for letra in palavra:
    if letra == 'a':
        contador += 1

print(f'A letra "a" aparece {contador} vezes.')