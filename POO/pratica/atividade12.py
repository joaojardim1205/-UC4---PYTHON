# Crie um iterador Pagina que receba uma lista e um tamanho de página (tamanho), e retorne sublistas (páginas) de acordo com o tamanho.

class Pagina:
    def __init__(self, lista, tamanho):
        self.lista = lista
        self.tamanho = tamanho
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.lista):
            raise StopIteration
        inicio = self.indice
        fim = inicio + self.tamanho
        self.indice = fim
        return self.lista[inicio:fim]

paginas = Pagina([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
for pagina in paginas:
    print(pagina)
