# Crie classes Voavel (com método voar()) e Nadavel (com método nadar()). Depois, crie uma classe Pato que herde de ambas e implemente esses métodos.

class Voavel:
    def voar(self):
        return "Voando..."

class Nadavel:
    def nadar(self):
        return "Nadando..."

class Pato(Voavel, Nadavel):
    def voar(self):
        return "Pato voando baixo."

    def nadar(self):
        return "Pato nadando no lago."

pato = Pato()
print(pato.voar())
print(pato.nadar())
