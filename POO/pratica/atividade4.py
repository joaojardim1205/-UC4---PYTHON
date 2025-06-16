# Crie uma classe Animal com o método fazer son) que retoma "Som genérica. Em seguida, crie subclasses Cachorro e Gato que sobrescrevam esse método com sons especificos.

class Animal:
    def fazer_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

cachorro = Cachorro()
gato = Gato()

print(cachorro.fazer_som())
print(gato.fazer_som())
