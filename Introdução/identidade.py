lista1 = [1, 2, 3]
lista2 = lista1
lista3 = [1, 2, 3]

print('Lista 1 é Lista 2?', lista1 is lista2)
print('Lista 1 é Lista 3?', lista1 is lista3)
print('Lista 1 não é Lista 3?', lista1 is not lista3)