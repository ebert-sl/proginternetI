# 5) Crie um script que busque no google. Utilize a url:
# http://www.google.com/search. Além disso, passe um parâmetro chamado “q”
# com o valor a ser buscado.

import requests
import requests_cache
from bs4 import BeautifulSoup

params = {
  'q': 'python'
}

requests_cache.install_cache('site_cache')
response = requests.get('http://www.google.com/search', params = params)

soup = BeautifulSoup(response.text, 'html.parser')
headers = soup.find_all('h3')

posicao = 1
for header in headers:
  print(posicao, " - ", header.get_text())
  posicao += 1