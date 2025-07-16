# Enunciado: Crie duas classes: Cachorro e Gato, cada uma com um método falar() (retorna "Oi, eu sou o Rex e "Oi, eu sou a Mili", respectivamente). Em seguida, crie uma função animal_fala() que aceita qualquer objeto com falar()

class Cachorro:
    def falar(self):
        return "Oi, eu sou o Rex"
    
class Gato:
    def falar(self):
        return "Oi, eu sou a Mili"
    
def animal_fala(animal):
        print(animal.falar())

cachorro = Cachorro()
gato = Gato()
animal_fala(cachorro)
animal_fala(gato)