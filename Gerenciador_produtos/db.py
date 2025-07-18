import sqlite3
def conectar():
    return sqlite3.connect("produtos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTEGER,
    valor REAL
    )
""")
    conn.commit()
    conn.close()

def inserir_produto(nome, quantidade, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, quantidade, valor) VALUES (?, ?, ?)",
    (nome, quantidade, valor))
    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    resultado = cursor.fetchall()
    conn.close()
    return resultado

def atualizar_produto(id, nome, quantidade, valor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE produtos SET nome=?, quantidade=?, valor=? WHERE id=?",
    (nome, quantidade, valor, id))
    conn.commit()
    conn.close()
    
def excluir_produto(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM produtos WHERE id=?", (id,))
    conn.commit()
    conn.close()