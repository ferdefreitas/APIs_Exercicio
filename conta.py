import sqlite3

'''
A tabela tem uma restrição CHECK (saldo >= 0) de propósito: o próprio
SQLite vai recusar um UPDATE que deixaria alguém com saldo negativo,
levantando sqlite3.IntegrityError. É essa exceção que seu código
precisa capturar pra fazer o rollback.

'''

def criar_tabela_contas(caminho_banco: str):
    """
    Cria a tabela `contas` com as colunas:
      id      INTEGER PRIMARY KEY
      titular TEXT NOT NULL
      saldo   INTEGER NOT NULL, com CHECK (saldo >= 0)
    Não esqueça do conn.commit() no final.

    """
    conn = sqlite3.connect(caminho_banco)
    conn.execute("CREATE TABLE IF NOT EXISTS contas"
    "(id INTEGER PRIMARY KEY," \
    "titular TEXT NOT NULL," \
    "saldo INTEGER NOT NULL CHECK (saldo >= 0))")
    conn.commit()
    conn.close()

def saldo_de(caminho_banco, id_conta):
    conn = sqlite3.connect(caminho_banco)
    saldo = conn.execute(
        "SELECT saldo FROM contas WHERE id = ?", (id_conta,)
    ).fetchone()[0]
    conn.close()
    return saldo