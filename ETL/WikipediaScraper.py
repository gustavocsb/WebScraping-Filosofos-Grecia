from bs4 import BeautifulSoup
import requests
import roman

url = 'https://pt.wikipedia.org/wiki/Lista_de_fil%C3%B3sofos_da_Gr%C3%A9cia_Antiga'
pagina = requests.get(url)
soup = BeautifulSoup(pagina.text, 'html.parser')

# Class da tabela descoberta inspecionando a página: <table class= "wikitable sortable jquery-tablesorter">

# Pegando todas as tabelas e achando a tabela onde estão os dados que serão extraídos, usando índice
tabela = soup.find_all('table')[1]

# Meio alternativo, pegando a tabela com a class dos dados que serão extraídos
# soup.find('table', class_ = 'wikitable sortable')

titulos = tabela.find_all('th')

tabela_titulos = [titulo.text.strip() for titulo in titulos]

import pandas as pd

df = pd.DataFrame(columns = tabela_titulos)

# Os dados dentro desta table estão dentros de tr(rows) e td(data)

coluna_dados = tabela.find_all('tr')

limpar_escola = ['?']

for linha in coluna_dados[1:]:
    linha_dados = linha.find_all('td')
    individual_linha_dados = [data.text.strip() for data in linha_dados]

    for string in limpar_escola:
        individual_linha_dados[2] = individual_linha_dados[2].replace(string, ' ')  # 

    # Corrigindo 2 linhas onde não estava puxando a última coluna 'Notas', sem dados no site
    while len(individual_linha_dados) < len(df.columns):
        individual_linha_dados.append('')

    tamanho = len(df)
    df.loc[tamanho] = individual_linha_dados

print(df)

df.to_excel(r'ETL\Filosofos.xlsx', index=False)