# Crie uma classe Minhal ista que implementa en getiten para funcionar com len() e indexação.

class MinhaLista:
    def __init__(self, dados):
        self.dados = dados

    def __getitem__(self, indice):
        return self.dados[indice]

    def __len__(self):
        return len(self.dados)

lista = MinhaLista([10, 20, 30, 40])
print(len(lista))
print(lista[2])
