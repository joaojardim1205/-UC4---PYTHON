import tkinter as tk
from db import listar_livros

def tela_listagem():
    janela = tk.Toplevel()
    janela.title("Listagem de Livros")
    janela.geometry("500x300")

    livros = listar_livros()

    texto = tk.Text(janela)
    texto.pack(expand=True, fill='both')

    texto.insert(tk.END, f"{'ID':<5} {'Nome do Livro':<20} {'Código':<15} {'Quantidade':<10}\n")
    texto.insert(tk.END, "-"*60 + "\n")

    for livro in livros:
        id, nome_livro, cod_livro, quantidade = livro
        texto.insert(tk.END, f"{id:<5} {nome_livro:<20} {cod_livro:<15} {quantidade:<10}\n")

    texto.config(state='disabled')
