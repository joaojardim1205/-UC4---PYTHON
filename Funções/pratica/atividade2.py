# Enunciado: Crie uma função eh_par que recebe um número e retoma True se for par e False se for Impar. Teste com 4 e 7

def eh_par(numero):
    return numero % 2 == 0

print("4 é par?", eh_par(4))
print("7 é par?", eh_par(7))
