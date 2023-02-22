# 1) Baixe uma página e exiba seus links. Para isso, extraia o atributo href das tags <a>.

import requests
import requests_cache
from bs4 import BeautifulSoup

requests_cache.install_cache('site_cache')
response = requests.get('https://alwaysjudgeabookbyitscover.com/')

soup = BeautifulSoup(response.text, 'html.parser')
cabecalhos = soup.find_all('a')

for link in cabecalhos:
  print(" - ", link.get('href'))