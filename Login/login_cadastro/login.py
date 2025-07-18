import tkinter as tk
from tkinter import messagebox
import sqlite3

# === Banco de Dados ===
def criar_banco():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT.
            login TEXT UNIQUE,
            senha TEXT
        )
    """)
    conexao.commit()
    conexao.close()

# === Funções de Autenticação ===
def logar():
    login = entry_login.get()
    senha = entry_senha.get()
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usarios WHERE login=? AND senha=? ", (login, senha))
    if cursor.fetchone():
        messagebox.showinfo("Sucesso", f"Bem-vindo, (login)!")
    else:
        messagebox.showerror("Erro", "Login ou senha incorretos.")
    conn.close()

def recuperar_senha():
    login = entry_login.get()
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT senha FROM usuarios WHERE login=?", (login,))
    resultado = cursor.fetchone ()
    if resultado:
        messagebox.showinfo("Recuperação de Senha", f"A senha é: (resultado [0])")
    else:
        messagebox.showerror("Erro", "Usuário não encontrado.")
    conn.close()

#=== Tela de Cadastro ===
def janela_cadastro():
    cadastro = tk. Toplevel ()
    cadastro.title("Cadastro de Usuário")
    cadastro.geometry("300x200")

    tk. Label (cadastro, text="Novo Login:").pack()
    novo_login = tk. Entry (cadastro)
    novo_login.pack()

    tk. Label (cadastro, text="Nova Senha:").pack()
    nova_senha = tk.Entry (cadastro, show="*")
    nova_senha.pack()

    def cadastrar_usuario(): 
        login = novo_login.get()
        senha = nova_senha.get()
        conn = sqlite3.connect("usuarios.db") 
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (login, senha) VALUES (?, ?)", (login, senha))
            conn.commit()
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            cadastro.destroy()
        except sqlite3. IntegrityError:
            messagebox.showerror("Erro", "Login já existe.")
        conn.close()
        
    tk.Button (cadastro, text="Cadastrar", command=cadastrar_usuario).pack(pady=10)

#=== Interface Gráfica ===
root = tk.Tk()
root.title("Sistema de Login")
root.geometry ("300x270")

tk. Label (root, text="FAÇA SEU LOGIN", font=("Helvetica", 14)).pack(pady=10)

tk. Label (root, text="Login:").pack()
entry_login = tk. Entry (root)
entry_login.pack()

tk. Label (root, text="Senha:").pack()
entry_senha = tk. Entry (root, show="*")
entry_senha.pack()

tk.Button(root, text="Logar", command=logar).pack (pady=5)
tk.Button (root, text="Cadastrar", command=janela_cadastro).pack(pady=5)
tk. Button (root, text="Recuperar Senha", command=recuperar_senha).pack (pady=5)
tk. Button (root, text="Sair", command=root.destroy).pack()

criar_banco ()
root.mainloop()