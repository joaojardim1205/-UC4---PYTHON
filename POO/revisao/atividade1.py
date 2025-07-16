#Enunciado: Crie uma classe Veiculo com os atributos marca e ano, e um método detalhes()que retorna uma string com essas informações. Em seguida, crie uma classe Carro que herda de Veiculo e adiciona o atributo portas. Sobrescreva o método detalhes() para incluir o número de portas.
class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}, Ano: {self.ano}"

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def detalhes(self):
        return f"{super().detalhes()}, Portas: {self.portas}"

carro = Carro("Toyota", 2020, 4)
print(carro.detalhes())