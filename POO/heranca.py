class animal:
    def __init__(self, nome) -> None:
        self.nome = nome
    
    def fazer_som(self):
        print('Som generico de animal')

class gato(animal):
    def fazer_som(self):
        print(f'{self.nome} diz: Miau!')

bichano = gato('Bichano')
mimosa = animal('Mimosa')

bichano.fazer_som()
mimosa.fazer_som()

                                                                 