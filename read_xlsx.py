import os
import pandas as pd

dir = os.getcwd()
data = os.path.join(dir, 'data')

# URL de um arquivo Excel hospedado no GitHub (com ?raw=True para baixar o conteúdo)
url = 'https://github.com/alura-cursos/Pandas/blob/main/emissoes_CO2.xlsx?raw=True'
dados_co2 = pd.read_excel(url)   
dados_co2.head()                  

# Exibe os nomes das abas (sheets) disponíveis no arquivo Excel
print(pd.ExcelFile(url).sheet_names)

# Lê a aba chamada 'fontes' do Excel
fontes = pd.read_excel(url, sheet_name='fontes')
fontes.to_excel(os.path.join(data, 'fontes.xlsx'), index=False)
                    
# Lê colunas A até D da aba 'emissoes_C02'
intervalo = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D')
intervalo.to_excel(os.path.join(data, 'intervalo.xlsx'), index=False)
                 
# Lê colunas A até D da aba 'emissoes_C02', apenas as 10 primeiras linhas
intervalo_2 = pd.read_excel(url, sheet_name='emissoes_C02', usecols='A:D', nrows=10)
intervalo_2.to_excel(os.path.join(data, 'intervalo_2.xlsx'), index=False)

