# Crie uma variável global total. Defina uma função adicionar (valor) que modifica total usando global

total = 0

def adicionar(valor):
    global total
    total += valor

adicionar(5)
print(total)

adicionar(10)
print(total)
