from bs4 import BeautifulSoup
import requests

url = 'https://pt.wikipedia.org/wiki/Lista_de_fil%C3%B3sofos_da_Gr%C3%A9cia_Antiga'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

# <table class= "wikitable sortable jquery-tablesorter">

# Pegando todas as tabelas e achando o dado que será extraído com índice
table = soup.find_all('table')[1]

# Meio alternativo, pegando a tabela com a class dos dados que serão extraídos
# print(soup.find('table', class_ = 'wikitable sortable'))

titles = soup.find_all('th')

print(titles)

table_titles = [title.text.strip() for title in titles]

print(table_titles)

