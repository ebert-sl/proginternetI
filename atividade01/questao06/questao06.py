# 6) Pesquise alguma página com uma tabela de classificação e extraia dessa
# página a tabela.

import requests
import requests_cache
from bs4 import BeautifulSoup
import pandas

requests_cache.install_cache('site_cache')
response = requests.get('https://brawlify.com/brawlers/detail/Sam')

soup = BeautifulSoup(response.text, 'html.parser')
tabela = soup.find('table')

headers = []
for index in tabela.find_all('th'):
  titulo = index.text
  headers.append(titulo)

tabela_extraida = pandas.DataFrame(columns = headers)

for dado in tabela.find_all('tr', class_="brawlerList-default"):
  dados_linha = dado.find_all('td')
  linha = [dado.get_text() for dado in dados_linha]
  comprimento = len(tabela_extraida)
  tabela_extraida.loc[comprimento] = linha

print(tabela_extraida)