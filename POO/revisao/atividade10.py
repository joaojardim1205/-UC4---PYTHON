# Enunciado: Crie uma classe Pai com um atributo valor = 10 e uma classe Filho que herda de Pai e modifica valor para 20. Mostre a diferença entre acessar o atributo pela classe pai e pela classe filho.

class Pai:
    valor = 10

class Filho(Pai):
    valor = 20

print(f"Atributo valor na classe Pai: {Pai.valor}")
print(f"Atributo valor na classe Filho: {Filho.valor}")