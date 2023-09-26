import pyodbc
import os
from utils import *


def retornar_cursor_banco_dados():
   # Metodo via inserção manual de parametros da conexão 
   # connection = pyodbc.connect(retorna_conexao_banco_dados())

   # Metodo de conexão via User DSN criada dentro do ODBC Client com nome ada
   # Detalhes abaixo em "Conexão via Trusted Connection (ODBC)"
   connection = pyodbc.connect('DSN=ada;Trusted_Connection=yes;')
   cursor = connection.cursor()
   return cursor, connection

def lista_banco_dados():
   cursor, connection = retornar_cursor_banco_dados()
   cursor.execute("select * from projeto_ada_giuliano.clientes;")
   clientes = cursor.fetchall()
   print("Dados de Todos os Clientes Cadastrados")
   print("")
   print(clientes)
   connection.commit()


def select_banco_dados(cpf):
   cursor, connection = retornar_cursor_banco_dados()
   cursor.execute("select * from projeto_ada_giuliano.clientes where cpf = '" + cpf + "';")
   clientes = cursor.fetchall()
   os.system('cls')
   print("Dados Cadastrais do Cliente")
   print("")
   print("Nome: ",clientes[0][1])
   print("CPF: ",clientes[0][0])
   print("RG: ",clientes[0][2])
   print("CEP: ", clientes[0][4])
   print("Logradouro: ", clientes[0][7])
   print("Numero: ", clientes[0][5])
   print("Complemento: ", clientes[0][6])
   print("Bairro: ", clientes[0][8])
   print("Cidade: ", clientes[0][9])
   print("UF: ", clientes[0][10])
   print("")
   connection.commit()


def insert_banco_dados(clientes):
   cursor, connection = retornar_cursor_banco_dados()
   insert_query = '''
   insert into projeto_ada_giuliano.clientes (nome, cpf, rg, nascimento, cep, logradouro, bairro, cidade, uf, numero, complemento)
   values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
   '''
   
   input_values = (clientes["Nome"], clientes["CPF"], clientes["RG"], clientes["Nascimento"], clientes["Endereco"]["CEP"], clientes["Endereco"]["Logradouro"], clientes["Endereco"]["Bairro"], clientes["Endereco"]["Cidade"], clientes["Endereco"]["UF"], clientes["Numero"], clientes["Complemento"])

   cursor.execute(insert_query, input_values)
   print("Cliente de CPF ",clientes["CPF"]," inserido com sucesso!")
   connection.commit()


def delete_banco_dados(cpf):
   cursor, connection = retornar_cursor_banco_dados()
   delete_query = "delete from projeto_ada_giuliano.clientes where cpf = '" + cpf + "';"

   cursor.execute(delete_query)
   print("Cliente de CPF ",cpf," deletado com sucesso!")
   connection.commit()


def update_banco_dados(cpf):
   cursor, connection = retornar_cursor_banco_dados()

   clientes = {
      "Nome": input("Atualize o Nome do Cliente: "),
      "CPF": valida_cpf(input("Atualize o CPF: ")),
      "RG": valida_rg(input("Atualize o RG: (xx.xxx.xxx-x) ")),
      "Nascimento": valida_data_nascimento(),
      "Endereco": busca_cep(input("Atualize o CEP: ")),
      "Numero": input("Atualize o número da residência: "),
      "Complemento": input("Atualize o complemento (apto, sobrado, referência): ")
   }

   update_query = "update projeto_ada_giuliano.clientes set nome = ?, cpf = ?, rg = ?, nascimento = ?, cep = ?, logradouro = ?, bairro = ?, cidade = ?, uf = ?, numero = ?, complemento = ?" + " where cpf = '" + cpf + "';"

   input_values = (clientes["Nome"], clientes["CPF"], clientes["RG"], clientes["Nascimento"], clientes["Endereco"]["CEP"], clientes["Endereco"]["Logradouro"], clientes["Endereco"]["Bairro"], clientes["Endereco"]["Cidade"], clientes["Endereco"]["UF"], clientes["Numero"], clientes["Complemento"])
   cursor.execute(update_query, input_values)
   print("Cliente de CPF anterior ",cpf," atualizado com sucesso para CPF", clientes["CPF"],"!")
   connection.commit()


#clientes = {'Nome': 'Augusto José', 'CPF': '56273515001', 'RG': '12.345.678-9', 'Nascimento': '04/13/2000', 'Endereco': {'CEP': '80050-390', 'Logradouro': 'Rua Eduardo Aguirre Calabresi', 'Bairro': 'Cristo Rei', 'Cidade': 'Curitiba', 'UF': 'PR'}, 'Numero': '432', 'Complemento': '2o andar'}


# Escolha qual funcao a ser testada
#insert_banco_dados(clientes)
#delete_banco_dados(clientes["CPF"])
#update_banco_dados(clientes["CPF"])
#select_banco_dados(clientes["CPF"])


# Conexão via Trusted Connection (ODBC)
# conn = pyodbc.connect('DSN=ada;Trusted_Connection=yes;')
#
# Configuração feita no ODBC Client
""" Microsoft SQL Server Native Client Version 11.00.7462
Data Source Name: ada
Data Source Description: Projeto Ada Giuliano
Server: hoesql633
Use Integrated Security: Yes
Database: SkillUp_GCOLIV1
Language: (Default)
Data Encryption: No
Trust Server Certificate: No
Multiple Active Result Sets(MARS): No
Mirror Server: 
Translate Character Data: Yes
Log Long Running Queries: No
Log Driver Statistics: No
Use Regional Settings: No
Use ANSI Quoted Identifiers: Yes
Use ANSI Null, Paddings and Warnings: Yes """

# Metodo de conexao anterior
""" def retorna_conexao_banco_dados():
    return(
    "DRIVER={SQL Server};"
    "SERVER=HOESQL633;"
    "DATABASE=SkillUp_GCOLIV1;"
    "Trusted_connection=yes;"
  ) """