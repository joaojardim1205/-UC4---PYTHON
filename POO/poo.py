class cachorro:
    # Atributo ou Variavel da classse
    especie = 'Canis Lupus Familiaris'

    # Metodo Construtor
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Metodo da classe
    def latir(self):
        print(f'{self.nome} diz: Ola cambada!')

 # Criando objeto
rex = cachorro('Rex', 3)
luna = cachorro('Luna', 5)

# Acessando atributos e metodos
print(rex.nome)
print(luna.idade)

luna.latir()
rex.latir()