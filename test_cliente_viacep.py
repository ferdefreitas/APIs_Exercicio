"""
Não mude este arquivo -- ele é a especificação. Seu trabalho é fazer
cliente_viacep.py passar em todos esses testes.

Rode com: pytest test_cliente_viacep.py -v
"""
import pytest
from unittest.mock import patch, MagicMock

from cliente_viacep import (
    consultar_endereco,
    validar_formato,
    CepInvalidoError,
    CepNaoEncontradoError,
)


# ---------- testes puros, sem rede (caso normal / limite / erro) ----------

def test_validar_formato_aceita_cep_com_hifen():
    assert validar_formato("80000-000") == "80000000"


def test_validar_formato_rejeita_cep_curto():
    with pytest.raises(CepInvalidoError):
        validar_formato("123")


def test_validar_formato_rejeita_cep_vazio():
    with pytest.raises(CepInvalidoError):
        validar_formato("")


# ---------- testes que "fingem" a chamada de rede com mock ----------

@patch("cliente_viacep.requests.get")
def test_consultar_endereco_caso_normal(mock_get):
    resposta_falsa = MagicMock()
    resposta_falsa.status_code = 200
    resposta_falsa.json.return_value = {
        "cep": "80000-000",
        "logradouro": "Rua Exemplo",
        "bairro": "Centro",
        "localidade": "Curitiba",
        "uf": "PR",
        "erro": False,
    }
    mock_get.return_value = resposta_falsa

    resultado = consultar_endereco("80000-000")

    assert resultado["cidade"] == "Curitiba"
    assert resultado["estado"] == "PR"
    mock_get.assert_called_once()


@patch("cliente_viacep.requests.get")
def test_consultar_endereco_nao_encontrado(mock_get):
    resposta_falsa = MagicMock()
    resposta_falsa.status_code = 200
    resposta_falsa.json.return_value = {"erro": True}
    mock_get.return_value = resposta_falsa

    with pytest.raises(CepNaoEncontradoError):
        consultar_endereco("00000-000")


def test_consultar_endereco_formato_invalido_nao_chama_rede():
    with pytest.raises(CepInvalidoError):
        consultar_endereco("abc")
