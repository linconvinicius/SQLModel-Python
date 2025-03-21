# SQLModel-Python

Este projeto demonstra como usar o SQLModel para conectar um aplicativo Python a um banco de dados SQLite. Ele inclui a criação de um modelo de dados, a configuração de uma conexão com o banco de dados e a execução de operações básicas de CRUD.

## Estrutura do Projeto

- **app.py**: Define o modelo de dados `Usuario` e configura a conexão com o banco de dados SQLite.
- **template.py**: Insere um registro no banco de dados e realiza uma consulta para listar todos os usuários.
- **database.db**: Arquivo do banco de dados SQLite gerado automaticamente.

## Requisitos

- Python 3.10 ou superior
- Biblioteca `sqlmodel`

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/linconvinicius/SQLModel-Python.git
   cd SQLModel-Python
   ```

2. Instale as dependências:
   ```bash
   pip install sqlmodel
   ```

## Como Usar

1. Execute o arquivo `app.py` para criar o banco de dados:
   ```bash
   python app.py
   ```

2. Execute o arquivo `template.py` para inserir dados e consultar o banco:
   ```bash
   python template.py
   ```

## Exemplo de Saída

Ao executar o `template.py`, você verá uma saída semelhante a esta:
```plaintext
[Usuario(id=1, nome='Teste', idade=32, email='teste@teste.com')]
```
