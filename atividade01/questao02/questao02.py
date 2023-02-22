# 2) Baixe uma página e exiba o conteúdo de uma determinada tag lida pelo teclado.

import requests
import requests_cache
from bs4 import BeautifulSoup

tag = input("Digite a tag que deseja pesquisar: ")

requests_cache.install_cache('site_cache')
response = requests.get('https://alwaysjudgeabookbyitscover.com/')

soup = BeautifulSoup(response.text, 'html.parser')
cabecalhos = soup.find_all(tag)

for tag in cabecalhos:
  print(" - ", tag.get_text())