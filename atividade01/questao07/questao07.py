# 7) Crie um script que lê um CEP e pesquise o endereço completo em alguma API
# aberta.

from pycep_correios import get_address_from_cep, WebService

cep = input("Digite um CEP para ver o endereço completo: ")
endereco = get_address_from_cep(cep, webservice=WebService.CORREIOS)

print(endereco)