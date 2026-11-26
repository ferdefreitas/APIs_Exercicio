"""
Não mude este arquivo -- ele é a especificação.
Rode com: pytest test_transferencia.py -v
"""
import sqlite3
import pytest
import transferencia


@pytest.fixture
def banco_temporario(tmp_path):
    caminho = str(tmp_path / "banco_teste.db")
    transferencia.criar_tabela_contas(caminho)

    conn = sqlite3.connect(caminho)
    conn.execute("INSERT INTO contas (id, titular, saldo) VALUES (1, 'Ana', 100)")
    conn.execute("INSERT INTO contas (id, titular, saldo) VALUES (2, 'Joao', 50)")
    conn.commit()
    conn.close()

    return caminho


def saldo_de(caminho_banco, id_conta):
    conn = sqlite3.connect(caminho_banco)
    saldo = conn.execute(
        "SELECT saldo FROM contas WHERE id = ?", (id_conta,)
    ).fetchone()[0]
    conn.close()
    return saldo


def test_transferencia_com_saldo_suficiente(banco_temporario):
    transferencia.transferir(banco_temporario, id_origem=1, id_destino=2, valor=30)

    assert saldo_de(banco_temporario, 1) == 70
    assert saldo_de(banco_temporario, 2) == 80


def test_transferencia_sem_saldo_suficiente_desfaz_tudo(banco_temporario):
    with pytest.raises(sqlite3.IntegrityError):
        transferencia.transferir(banco_temporario, id_origem=1, id_destino=2, valor=500)

    # prova de que o rollback funcionou: nenhum saldo mudou
    assert saldo_de(banco_temporario, 1) == 100
    assert saldo_de(banco_temporario, 2) == 50
