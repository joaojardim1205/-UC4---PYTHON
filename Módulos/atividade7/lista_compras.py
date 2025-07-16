# Crie um módulo lista_compras.py com: Uma lista global itens = []. Função adicionar_item(item) que adiciona um item à lista. Função mostrar_itens() que exibe todos os itens.

itens = []

def adicionar_item(item):
    itens.append(item)

def mostrar_itens():
    if not itens:
        print("A lista de compras está vazia.")
    else:
        print("Itens na lista de compras:")
        for item in itens:
            print(f"- {item}")