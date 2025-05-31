import os
import json
import pandas as pd

dir = os.getcwd()
data = os.path.join(dir, 'data')

# Lê o arquivo 'pacientes.json' diretamente como um DataFrame
df_pacientes = pd.read_json(os.path.join(data, 'pacientes.json'))
df_pacientes.head()        

# Abre e carrega manualmente o arquivo 'pacientes_2.json' como dicionário (JSON)
with open(os.path.join(data, 'pacientes_2.json'),'r') as f:
    dados_json = json.loads(f.read())

# Normaliza a estrutura JSON aninhada: extrai os registros de 'Pacientes', mantendo 'Pesquisa' e 'Ano'
df_pacientes_2_normalize = pd.json_normalize(dados_json, record_path='Pacientes', meta=['Pesquisa', 'Ano'])

# Exporta o DataFrame normalizado para um novo arquivo JSON
df_pacientes_2_normalize.to_json(os.path.join(data,'pacientes_2_normalize.json'))

# Mostra as 5 primeiras linhas do DataFrame normalizado
df_pacientes_2_normalize.head()