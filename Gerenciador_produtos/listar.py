import tkinter as tk
from tkinter import messagebox
from db import listar_produtos, excluir_produto, atualizar_produto

def tela_listagem():
    janela = tk. Toplevel()
    janela.title("Lista de Produtos")
    janela.geometry("400x300")

    produtos = listar_produtos()
    for produto in produtos:
        frame = tk. Frame(janela)
        frame.pack(pady=5, fill="x")

        id, nome, quantidade, valor = produto

        label = tk.Label(frame, text=f"{id} - {nome} - Qtd: {quantidade} - R${valor:.2f}", anchor="w")
        label.pack(side="left", padx=5)
        
    def deletar(prod_id=id):
        excluir_produto(prod_id)
        messagebox.showinfo("Removido", "Produto excluído.")
        janela.destroy()
        tela_listagem()

    def editar(prod_id=id):
        editar_janela = tk. Toplevel()
        editar_janela.title("Editar Produto")

        tk. Label(editar_janela, text="Nome:").pack()
        novo_nome = tk. Entry(editar_janela)
        novo_nome.insert(0, nome)
        novo_nome.pack()

        tk.Label(editar_janela, text="Quantidade:").pack()
        nova_quant = tk.Entry(editar_janela)
        nova_quant.insert(0, quantidade)
        nova_quant.pack()

        tk.Label(editar_janela, text="Valor.").pack()
        novo_valor = tk.Entry(editar_janela)
        novo_valor.insert(0, valor)
        novo_valor.pack()
        
        def salvar():
            try:
                atualizar_produto(prod_id, novo_nome.get(), int(nova_quant.get()).
                float(novo_valor.get()))
                messagebox.showinfo("Sucesso", "Produto atualizado.")
                editar_janela.destroy()
                janela.destroy()
                tela_listagem()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro: (e)")

        tk.Button(editar_janela, text="Salvar", command=salvar).pack(pady=10)
    tk.Button(frame, text="Editar", command=editar).pack(side="left", padx=5)
    tk. Button(frame, text="Excluir", command=deletar).pack(side="left", padx=5)