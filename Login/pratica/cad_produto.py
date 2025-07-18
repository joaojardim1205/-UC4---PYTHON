# Crie uma tela de 400 x 600 com os seguintes campos: nome_produto - quantidade - codigo - fabricante
# Crie os botões: Cadastrar - Sair

import tkinter as tk
from tkinter import messagebox

def cadastrar():
    nome_produto = entry_nome_produto.get()
    quantidade = entry_quantidade.get()
    codigo = entry_codigo.get()
    fabricante = entry_fabricante.get()

    if not nome_produto or not quantidade or not codigo or not fabricante:
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos.")
        return
    
    # Aqui você pode adicionar a lógica de cadastro do produto
    messagebox.showinfo("Cadastro", f"Produto: {nome_produto}\nQuantidade: {quantidade}\nCódigo: {codigo}\nFabricante: {fabricante}")

def sair():
    root.destroy()

# Janela principal
root = tk.Tk()
root.title("Cadastro de Produto")
root.geometry("400x400")

# Título
titulo = tk.Label(root, text="CADASTRO DE PRODUTO", font=("Helvetica", 16))
titulo.pack(pady=10)

# Campo de nome do produto
label_nome_produto = tk.Label(root, text="Nome do Produto:")
label_nome_produto.pack()
entry_nome_produto = tk.Entry(root)
entry_nome_produto.pack(pady=5)

# Campo de quantidade
label_quantidade = tk.Label(root, text="Quantidade:")
label_quantidade.pack()
entry_quantidade = tk.Entry(root)
entry_quantidade.pack(pady=5)

# Campo de código
label_codigo = tk.Label(root, text="Código:")
label_codigo.pack()
entry_codigo = tk.Entry(root)
entry_codigo.pack(pady=5)

# Campo de fabricante
label_fabricante = tk.Label(root, text="Fabricante:")
label_fabricante.pack()
entry_fabricante = tk.Entry(root)
entry_fabricante.pack(pady=5)

# Botões
botao_cadastrar = tk.Button(root, text="Cadastrar", command=cadastrar)
botao_cadastrar.pack(pady=10)
botao_sair = tk.Button(root, text="Sair", command=sair)
botao_sair.pack(pady=5)

root.mainloop()