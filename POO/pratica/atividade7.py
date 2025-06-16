# Adicione um método estático eh adulto (idade) à classe Pessoa que retorne True se a idade for >= 18.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def eh_adulto(idade):
        return idade >= 18

print(Pessoa.eh_adulto(20))
print(Pessoa.eh_adulto(15))
