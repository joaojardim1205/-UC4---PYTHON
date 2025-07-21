import sqlite3

def conectar():
    return sqlite3.connect("biblioteca.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_livro TEXT NOT NULL,
        cod_livro TEXT NOT NULL,
        quantidade INTEGER NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

def inserir_livro(nome_livro, cod_livro, quantidade):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO livros (nome_livro, cod_livro, quantidade) VALUES (?, ?, ?)",
                   (nome_livro, cod_livro, quantidade))
    conexao.commit()
    conexao.close()

def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM livros")
    resultado = cursor.fetchall()
    conexao.close()
    return resultado