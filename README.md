# Migrador de Dados de CNPJ para MySQL
Este é um script Python projetado para migrar dados de um banco de dados SQLite para um banco de dados MySQL. O script extrai informações de estabelecimentos de uma tabela SQLite e as insere em uma tabela MySQL após a aplicação de algumas transformações nos dados.

## Pré-requisitos
Python 3.x instalado
Biblioteca sqlite3 (inclusa na instalação padrão do Python)
Biblioteca mysql-connector-python (instalável via pip install mysql-connector-python)

## Configuração
Antes de executar o script, você precisa realizar algumas configurações:

Caminho do Arquivo SQLite: Certifique-se de alterar o caminho do arquivo SQLite (cnpj.db) para o local correto onde o arquivo está armazenado no seu sistema.

Conexão MySQL: Verifique se as credenciais de conexão ao MySQL (host, user, password, database) estão corretas e correspondem à configuração do seu ambiente.

# Execução
Para executar o script, basta rodar o código Python fornecido.

```
python index.py
```
Certifique-se de estar no diretório correto onde o script está localizado.
