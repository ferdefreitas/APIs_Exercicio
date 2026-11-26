"""
DESAFIO: consumir a API pública ViaCEP (https://viacep.com.br/ws/{cep}/json/).

Preencha as funções abaixo. Rode `pytest test_cliente_viacep.py -v` pra
ver quais passam. Os testes já estão prontos em test_cliente_viacep.py
e são a especificação do que cada função precisa fazer -- não mude os
testes, mude seu código até eles passarem.

DICA GERAL: comece pela função mais simples (limpar_cep), depois
validar_formato, e só por último consultar_endereco.
"""
import requests


class CepInvalidoError(Exception):
    """Lançado quando o CEP não tem o formato esperado."""
    pass


class CepNaoEncontradoError(Exception):
    """Lançado quando o CEP é bem formado mas não existe de verdade."""
    pass


def limpar_cep(cep: str) -> str:
    """
    Recebe um CEP em qualquer formato (ex: "80000-000", "80000000",
    "80.000-000") e devolve só os 8 dígitos, sem pontuação.

    TODO: implemente isso.
    """
    raise NotImplementedError


def validar_formato(cep: str) -> str:
    """
    Usa limpar_cep() e garante que sobraram exatamente 8 dígitos.
    Se não tiver 8 dígitos, deve levantar CepInvalidoError.
    Se estiver certo, devolve o CEP limpo.

    TODO: implemente isso.
    """
    raise NotImplementedError


def consultar_endereco(cep: str) -> dict:
    """
    1. Valida o formato do CEP (reaproveite validar_formato).
    2. Faz um GET em https://viacep.com.br/ws/{cep_limpo}/json/
    3. Se o status_code não for 200, levanta CepNaoEncontradoError.
    4. A ViaCEP tem uma peculiaridade: quando o CEP não existe, ela
       devolve status 200 mas com {"erro": true} no corpo. Você
       precisa checar isso manualmente e levantar CepNaoEncontradoError
       também nesse caso.
    5. Se deu tudo certo, devolve um dicionário só com as chaves:
       "cep", "logradouro", "bairro", "cidade", "estado"
       (repare que os nomes dos campos que a ViaCEP devolve são
       diferentes -- ela usa "localidade" e "uf", por exemplo).

    TODO: implemente isso.
    """
    raise NotImplementedError
