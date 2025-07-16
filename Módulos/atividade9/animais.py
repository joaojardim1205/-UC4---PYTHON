# Crie um módulo animais.py com: Classe Animal (atributo nome, método emitir_som()). Classe Cachorro que herda de Animal e sobrescreve emitir_som().

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        raise NotImplementedError("Subclasse deve implementar este método")
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"