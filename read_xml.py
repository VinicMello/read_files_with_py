import os
import pandas as pd

dir = os.getcwd()
data = os.path.join(dir, 'data')

# Lê um arquivo XML localizado no diretório 'data'
dados_xml = pd.read_xml(os.path.join(data, 'imdb_top_1000.xml'))

# Salva o DataFrame como arquivo XML no mesmo diretório
dados_xml.to_xml(os.path.join(data, 'dados_xml.xml'))
