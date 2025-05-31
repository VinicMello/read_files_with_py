import os
import pandas as pd

dir = os.getcwd()
data = os.path.join(dir, 'data')
dados_html = pd.read_html(os.path.join(data, 'filmes_wikipedia.html'))

# Itera sobre todas as tabelas lidas e salva cada uma como um novo arquivo HTML
counter = 1
for table in dados_html:
    table.to_html(os.path.join(data, f'table_{counter}.html'))
    counter = counter + 1
