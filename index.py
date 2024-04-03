import sqlite3
import mysql.connector
import random

# Função para gerar valores aleatórios para setor_id e porte_id
def gerar_valores_aleatorios():
    setor_id = random.randint(1, 6)
    porte_id = random.randint(1, 4)
    return setor_id, porte_id

#ATENÇÃO: Altere o caminho do arquivo .db para o caminho onde o arquivo cnpj.db está salvo
conn_sqlite = sqlite3.connect(r'C:\cnpj\cnpj\cnpj.db')
cursor_sqlite = conn_sqlite.cursor()

# Conectar ao banco de dados MySQL
conn_mysql = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='integrador'
)

cursor_mysql = conn_mysql.cursor()

consulta_sqlite = "SELECT nome_fantasia, empresas.razao_social, cnpj, cep, logradouro, numero, complemento FROM estabelecimento INNER JOIN empresas ON estabelecimento.cnpj_basico = empresas.cnpj_basico"

cursor_sqlite.execute(consulta_sqlite)

contador_linhas = 0
contador_commits = 0

# Iterar sobre os resultados e inserir na tabela MySQL
for row in cursor_sqlite:
    #Gerando os valores aleatorios para meus setores e portes
    setor_id, porte_id = gerar_valores_aleatorios()
    
    cursor_mysql.execute("INSERT INTO empresa (nome_fantasia, razao_social, cnpj, cep, logradouro, numero, complemento, setor_id, porte_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5], row[6], setor_id, porte_id))
    
    contador_linhas += 1
    
    # Fazer commit a cada 15 linhas inseridas
    if contador_linhas % 15 == 0:
        conn_mysql.commit()
        contador_commits += 1
        print(f"Commit {contador_commits} realizado. Linhas inseridas até agora: {contador_linhas}")

conn_mysql.commit()
contador_commits += 1

cursor_sqlite.close()
conn_sqlite.close()
cursor_mysql.close()
conn_mysql.close()

print("Dados migrados com sucesso!")
print(f"Total de commits realizados: {contador_commits}")