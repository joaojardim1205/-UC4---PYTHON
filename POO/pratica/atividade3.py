# Crie uma classe Veiculo com atributos marca e modelo. Depois, crie uma subclasse Carra que adicione o atributo portas (int), Instancie um carro e exiba seus detalhes

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def detalhes(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Portas: {self.portas}"

carro1 = Carro("Toyota", "Corolla", 4)
print(carro1.detalhes())