import tkinter as tk
from tkinter import messagebox

def logar():
    usuario = entry_login.get()
    senha = entry_senha.get()
    # Aqui você pode adicionar a lógica de verificação do login
    messagebox.showinfo("Login", f"Usuário: {usuario}\nSenha: {senha}")

def sair():
    root.destroy()

# Janela principal
root = tk.Tk()
root.title("Tela de Login")
root.geometry("300x200")

#Título
titulo = tk.Label(root, text="FAÇA SEU LOGIN", font=("Helvetica", 14))
titulo.pack(pady=10)

# Campo de login
label_login = tk.Label(root, text="Login:")
label_login.pack()
entry_login = tk.Entry(root)
entry_login.pack()

#Campo de senha
label_senha = tk.Label(root, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(root, show="+")
entry_senha.pack()

#Botões
botao_logar = tk.Button(root, text="Logar", command=logar)
botao_logar.pack(pady=5)
botao_sair = tk.Button(root, text="Sair", command=sair)
botao_sair.pack()
    
root.mainloop()