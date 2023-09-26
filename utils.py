from validate_docbr import CPF
from datetime import datetime
import re
import requests

def teste ():
    pass

def valida_cpf(cpf_input):
    cpf = CPF()
    while True:
       cpf_input = re.sub('[-.]','',cpf_input)
       resultado = cpf.validate(cpf_input)
       if resultado:
          cpf_formatado = f"{cpf_input[:3]}.{cpf_input[3:6]}.{cpf_input[6:9]}-{cpf_input[9:]}"
          return cpf_formatado
       else: cpf_input = input("CPF Inválido. Digite novamente: ")

def valida_rg(rg_input):

  padrao_rg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'
  while True:
     rg_input = re.sub('[-.]','',rg_input)
     rg_input = f"{rg_input[:2]}.{rg_input[2:5]}.{rg_input[5:8]}-{rg_input[8:]}"
     if re.match(padrao_rg, rg_input):
        return rg_input
     else:
        rg_input = input("RG Inválido. Digite novamente: ")

def valida_data_nascimento():
   while True:
      data_nascimento_input = input("Digite a data de nascimento (mm/dd/yyyy): ")
      try:
         data_convertida = datetime.strptime(data_nascimento_input,"%m/%d/%Y").date()
         data_atual = datetime.now().date()
         if data_convertida < data_atual:
            return data_convertida.strftime("%m/%d/%Y")
         else:
            data_nascimento_input = input("Data inválida. Data de nascimento é posterior à data de hoje!")
      except ValueError as cod_erro:
         print("Data com formato inválido. Código de erro: ", cod_erro)

### Codigo de busca de CEP a partir da API ViaCEP.com.br
def busca_cep(cep_input):
   api = f'https://viacep.com.br/ws/{cep_input}/json/'
   retorno_api = requests.get(api, verify=False)
   if retorno_api.status_code == 200:
      dados = retorno_api.json()
      endereco = {
         "CEP": dados['cep'],
         "Logradouro": dados['logradouro'],
         "Bairro": dados['bairro'],
         "Cidade": dados['localidade'],
         "UF": dados['uf']
      }
      return endereco


### Codigo de busca de CEP com validação manual   
""" def busca_cep(cep_input):
  # 00000-000
  padrao_cep = r'^\d{5}(-\d{3})?$'
  while True:
     cep_input = re.sub('[-.]','',cep_input)
     cep_input = f"{cep_input[:5]}-{cep_input[5:]}"
     if re.match(padrao_cep, cep_input):
        return cep_input
     else:
        cep_input = input("CEP Inválido. Digite o CEP novamente (00000-000): ") """