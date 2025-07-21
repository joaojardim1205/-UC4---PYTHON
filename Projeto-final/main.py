import tkinter as tk
from cadastro import tela_cadastro
from listar import tela_listagem
from db import criar_tabela

def main():
    criar_tabela()

    root = tk.Tk()
    root.title("Sistema de Cadastro Biblioteca")
    root.geometry("300x200")

    tk.Label(root, text="Gerenciador de Biblioteca", font=("Helvetica", 14)).pack(pady=10)
    tk.Button(root, text="Cadastrar Livro", command=tela_cadastro).pack(pady=5)
    tk.Button(root, text="Listar Livros", command=tela_listagem).pack(pady=5)
    tk.Button(root, text="Sair", command=root.destroy).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()