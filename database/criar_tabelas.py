import sqlite3

def criar_tabela():
    conn=sqlite3.connect("funcionario.db")
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS funcionario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NULL,
            data_nascimento DATE,
            genero TEXT NULL,
            estado_civil TEXT NULL,
            email TEXT NULL,
            telefone INTEGER
        )
    """)
    conn.commit()
    conn.close()


