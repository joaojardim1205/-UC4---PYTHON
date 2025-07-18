import tkinter as tk
from tkinter import messagebox
from db import inserir_produto

def tela_cadastro():
    janela = tk. Toplevel()
    janela.title("Cadastro de Produto")
    janela.geometry("300x250")

    tk.Label(janela, text="Nome:").pack()
    nome = tk.Entry(janela)
    nome.pack()

    tk.Label(janela, text="Quantidade:").pack()
    quantidade = tk.Entry(janela)
    quantidade.pack()

    tk.Label(janela, text="Valor:").pack()
    valor = tk.Entry(janela)
    valor.pack()

    def cadastrar():
        try:
            inserir_produto(nome.get(), int(quantidade.get()), float(valor.get()))
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
        
    tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=10)