import os
import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, inspect, text

dir = os.getcwd()
data = os.path.join(dir, 'data')
engine = create_engine('sqlite:///:memory:')
data_url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/clientes_banco.csv'

# Lê o arquivo CSV a partir da URL
dados = pd.read_csv(data_url)

# Salva os dados no banco de dados SQLite como a tabela 'clientes'
dados.to_sql('clientes', engine, index=False)

# Inspeciona o banco para verificar as tabelas disponíveis
inspector = inspect(engine)
print(inspector.get_table_names())

# Seleciona os registros da tabela 'clientes' cuja categoria de renda é "Empregado"
sql_empregado = '''
SELECT * FROM clientes WHERE categoria_de_renda = "Empregado"
'''
df_empregado = pd.read_sql(sql_empregado, engine)

# Salva os empregados em uma nova tabela chamada 'empregado'
df_empregado.to_sql('empregado', con=engine, index=False)

# Lê apenas algumas colunas da tabela 'empregado' e mostra as 5 primeiras linhas
select_df_empregado = pd.read_sql_table(
    'empregado', engine, 
    columns=['ID_Cliente', 'Grau_escolaridade', 'Rendimento_anual']
).head()
select_df_empregado.head()

# Seleciona todos os dados da tabela 'clientes'
sql_clientes = '''
SELECT * FROM clientes
'''
df_clientes = pd.read_sql(sql_clientes, engine)

# Deleta o cliente com ID específico (5008804) da tabela 'clientes'
sql_delete_row_id = '''
DELETE FROM clientes WHERE ID_Cliente = 5008804
'''
with engine.connect() as conn:
    conn.execute(text(sql_delete_row_id))
    conn.commit()

# Valida se o cliente foi realmente excluído
sql_valida = '''
SELECT * FROM clientes WHERE ID_Cliente = 5008804
'''
df_valida = pd.read_sql(sql_valida, engine)
df_valida.head()

# Corrige a escolaridade de um cliente específico (ID_Cliente = 5008808)
sql_update_row_id = '''
UPDATE clientes SET Grau_escolaridade = "Ensino Superior" WHERE ID_Cliente = 5008808
'''
with engine.connect() as conn:
    conn.execute(text(sql_update_row_id))
    conn.commit()

# Valida a atualização do cliente
sql_valida = '''
SELECT * FROM clientes WHERE ID_Cliente = 5008808
'''
df_valida = pd.read_sql(sql_valida, engine)
df_valida.head()
