# Crie uma classe base Veiculo com método mover() Derive Carro e Barco sobrescrevendo mover().

class Veiculo:
    def mover(self):
        print("O veículo está se movendo")

class Carro(Veiculo):
    def mover(self):
        print("O carro está dirigindo")

class Barco(Veiculo):
    def mover(self):
        print("O barco está navegando")

v = Veiculo()
c = Carro()
b = Barco()

v.mover()
c.mover()
b.mover()