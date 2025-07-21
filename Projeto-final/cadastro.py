import tkinter as tk
from tkinter import messagebox
from db import inserir_livro

def tela_cadastro():
    janela = tk.Toplevel()
    janela.title("Cadastro de Livro")
    janela.geometry("300x200")

    tk.Label(janela, text="Nome do Livro:").pack()
    nome_livro = tk.Entry(janela)
    nome_livro.pack()

    tk.Label(janela, text="Código do Livro:").pack()
    cod_livro = tk.Entry(janela)
    cod_livro.pack()

    tk.Label(janela, text="Quantidade:").pack()
    quantidade = tk.Entry(janela)
    quantidade.pack()

    def cadastrar():
        try:
            inserir_livro(nome_livro.get(), cod_livro.get(), int(quantidade.get()))
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")

    tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)
