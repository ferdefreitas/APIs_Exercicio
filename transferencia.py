"""
DESAFIO: transferência entre contas com TRANSAÇÃO.

Rode `pytest test_transferencia.py -v` pra ver se passa.

A tabela tem uma restrição CHECK (saldo >= 0) de propósito: o próprio
SQLite vai recusar um UPDATE que deixaria alguém com saldo negativo,
levantando sqlite3.IntegrityError. É essa exceção que seu código
precisa capturar pra fazer o rollback.
"""
import sqlite3


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


def transferir(caminho_banco: str, id_origem: int, id_destino: int, valor: int):
    """
    Debita `valor` da conta id_origem e credita na conta id_destino.
    As duas operações precisam acontecer na MESMA transação:

    - Se as duas derem certo: conn.commit()
    - Se qualquer uma falhar (sqlite3.IntegrityError, por exemplo
      porque o saldo ficaria negativo): conn.rollback() e relance o
      erro (raise), pra quem chamou saber que a transferência falhou.
    - De qualquer forma (deu certo ou não), feche a conexão no final.
    """
    try:
        conn = sqlite3.connect(caminho_banco)
        cursor = conn.cursor()
        cursor.execute("UPDATE contas SET saldo = saldo - ? WHERE id = ?", (valor, id_origem))
        cursor.execute("UPDATE contas SET saldo = saldo + ? WHERE id = ?", (valor, id_destino))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.rollback()
        raise
    finally:
        conn.close()
