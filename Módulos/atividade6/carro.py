# Crie um módulo carro.py com uma classe Carro: Atributos: marca, modelo, ano. Método detalhes() que retorna uma string com as informações.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"