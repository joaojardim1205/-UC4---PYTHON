# Enunciado: Crie uma classe Animal com o método comer(), e uma classe Voador com o método voar(). Em seguida, crie uma classe Morcego que herda de ambas e implementa um método detalhes() que chama os métodos das classes pai.
class Animal:
    def comer(self):
        return "O animal está comendo."

class Voador:
    def voar(self):
        return "O voador está voando."
    
class Morcego(Animal, Voador):
    def detalhes(self):
        return f"{self.comer()} {self.voar()}"
    
morcego = Morcego()
print(morcego.detalhes())