import os
import pandas as pd

dir = os.getcwd()
data = os.path.join(dir, 'data')

# Lê um arquivo CSV separado por vírgulas a partir de uma URL
url = 'https://raw.githubusercontent.com/alura-cursos/pandas/refs/heads/main/superstore_data.csv'
dados = pd.read_csv(url)
             
# Lê um CSV separado por ponto e vírgula (;) a partir de uma URL
url_ponto_e_virgula = 'https://raw.githubusercontent.com/alura-cursos/Pandas/refs/heads/main/superstore_data_ponto_virgula.csv'
dados_ponto_e_virgula = pd.read_csv(url_ponto_e_virgula, sep=';')

# Lê apenas as 5 primeiras linhas do CSV
dados_primeiras_linhas = pd.read_csv(url, nrows=5)

# Lê apenas as colunas 'Id', 'Year_Birth' e 'Income' pelo nome
dados_selecao = pd.read_csv(url, usecols=['Id', 'Year_Birth', 'Income'])

# Lê as colunas de índice 0, 1 e 4 (em vez de usar os nomes)
dados_selecao = pd.read_csv(url, usecols=[0, 1, 4])

# Salva o DataFrame como CSV com índice (padrão: index=True)
dados_selecao.to_csv(os.path.join(data, 'clientes_mercado.csv')) 

# Salva o CSV sem o índice (index=False)
dados_selecao.to_csv(os.path.join(data, 'dados_mercado.csv'), index=False)

print()
