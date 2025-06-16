# Crie uma classe livro com os atributos titulo (str), autor (str) e ano (int) Adicione um método detalhes) que retoma uma string formatada com essas informações. Instancie um objeto e chame o método

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}"

livro1 = Livro("1984", "George Orwell", 1949)
print(livro1.detalhes())
