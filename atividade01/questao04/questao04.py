# 4) Dado um endereço de uma imagem na internet, baixe o arquivo e salve-o
# localmente.

import requests

response = requests.get('https://www.python.org/static/img/python-logo.png')

with open("questao04\img_download\img.png", "wb") as file:
  file.write(response.content)