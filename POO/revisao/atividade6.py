# Enunciado: Crie uma classe Pessoa com um atributo de classe contador = 0 e um atributo de instância nome. Incremente contador no __init__ para contar quantas instâncias foram criadas. Mostre o escopo de cada atributo.

class Pessoa:
    contador = 0 
    
    def __init__(self, nome):
        self.nome = nome
        Pessoa.contador += 1

    def detalhes(self):
        return f"Nome: {self.nome}, Contador de instâncias: {Pessoa.contador}"

pessoa1 = Pessoa("Alice")
pessoa2 = Pessoa("Bob") 
print(pessoa1.detalhes())
print(pessoa2.detalhes()) 