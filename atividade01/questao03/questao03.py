# 3) Receba uma página como entrada e um termo a ser buscado e liste as
# ocorrências dentro dessa página. Atente para extrair o texto da página sem as
# tags e, ao encontrar uma ocorrência do termo, exiba os 20 caracteres antes e
# 20 caracteres depois.

import requests
import requests_cache
import re
from bs4 import BeautifulSoup

site = input("Digite o site que deseja analisar: ")
termo = input("Digite o termo que deseja procurar no site: ")

requests_cache.install_cache('site_cache')
response = requests.get(site)

soup = BeautifulSoup(response.text, 'html.parser')
conteudos = soup.find_all(string=re.compile(termo))

for conteudo in conteudos:
  inicio_termo = re.search(termo, conteudo).start()
  fim_termo = re.search(termo, conteudo).end()
  if inicio_termo <= 19:
    print(" - ", conteudo[0 : fim_termo + 20])
  else:
    print(" - ", conteudo[inicio_termo - 20 : fim_termo + 20])