# APIs_Exercicio

Exercícios práticos de Python com foco em **consumo de API REST**, **transações em banco de dados** e **testes automatizados com pytest**.

Cada exercício vem com um arquivo de testes que serve como especificação: o objetivo é fazer o código passar nos testes, sem alterar os testes.

## Exercícios

### 1. Cliente ViaCEP — `cliente_viacep.py`

Consulta endereços na API pública [ViaCEP](https://viacep.com.br/) a partir de um CEP.

| Função | O que faz |
|---|---|
| `limpar_cep(cep)` | Remove pontuação e devolve só os dígitos (`"80.000-000"` → `"80000000"`) |
| `validar_formato(cep)` | Garante que o CEP tem 8 dígitos; senão levanta `CepInvalidoError` |
| `consultar_endereco(cep)` | Faz o GET na ViaCEP e devolve `cep`, `logradouro`, `bairro`, `cidade` e `estado` |

Pontos de atenção:
- A ViaCEP responde **status 200 com `{"erro": true}`** quando o CEP não existe, então isso precisa ser tratado manualmente (`CepNaoEncontradoError`).
- Os testes usam **mock** (`unittest.mock.patch`) para simular a resposta da API, então rodam sem acesso à internet.

Status: 🚧 em andamento

### 2. Transferência entre contas — `transferencia.py` e `conta.py`

Transfere saldo entre duas contas em um banco **SQLite**, usando **transação**: as duas operações (débito e crédito) acontecem juntas ou nenhuma acontece.

- `conta.py`: cria a tabela `contas` (com `CHECK (saldo >= 0)`) e consulta saldo.
- `transferencia.py`: `transferir()` faz o débito e o crédito; se o saldo ficaria negativo, o SQLite levanta `IntegrityError`, o código faz `rollback()` e relança o erro.

Status: ✅ concluído

## Estrutura

```
APIs_Exercicio/
├── cliente_viacep.py        # exercício 1
├── test_cliente_viacep.py   # testes do exercício 1
├── conta.py                 # funções auxiliares da tabela de contas
├── transferencia.py         # exercício 2
├── test_transferencia.py    # testes do exercício 2
└── requirements.txt
```

## Como rodar

Requisitos: Python 3.10+.

```bash
# (opcional) criar e ativar um ambiente virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/macOS

# instalar dependências
pip install -r requirements.txt

# rodar todos os testes
pytest -v

# ou só um exercício
pytest test_cliente_viacep.py -v
pytest test_transferencia.py -v
```

## Tecnologias

- Python
- [requests](https://requests.readthedocs.io/) para chamadas HTTP
- [sqlite3](https://docs.python.org/3/library/sqlite3.html) (biblioteca padrão)
- [pytest](https://docs.pytest.org/) e `unittest.mock` para testes
