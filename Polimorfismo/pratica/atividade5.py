# Crie uma função processar texto (texto) que chama texte upper() e texto.lower().
# Teste com strings normais e uma classe personalizada que implemente esses métodos.

def processar_texto(texto):
    print(texto.upper())
    print(texto.lower())

processar_texto("Exemplo De Texto")

class MeuTexto:
    def __init__(self, conteudo):
        self.conteudo = conteudo

    def upper(self):
        return self.conteudo.upper()

    def lower(self):
        return self.conteudo.lower()

processar_texto(MeuTexto("Texto Personalizado"))
