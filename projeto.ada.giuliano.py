#import time
#import datetime
#import pandas as pd
#import pandas_datareader as pdr
from termcolor import colored
#from validate_docbr import CPF
from utils import *
import os
from sqlserverfunctions import *


# Clearing the Screen
#def cls(): print ("\n" * 100)

# from "file" import "function" *

os.system('cls')

#cls()
#print ("\n" * 100)
print(colored('Giuliano C Oliveira - Projeto Introducao Python ada - Dados da Bolsa de Valores via Yahoo Finance!','light_blue'))
print("")
print("INFORMAÇÃO IMPORTANTE")
print("")
print("Tickers de acões na B3, adicionar .SA como sufixo, p.ex: PETR4.SA")
print("Tickers de ações na NASDAQ ou Dow Jones não necessitam adicionar sufixo, p.ex: XOM")
print("")

menu_principal = True
lista_clientes = []
while menu_principal:
    print("")
    print(colored('Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações. Selecione uma das opções abaixo:','magenta'))
    print("1 - Cliente")
    print("2 - Ordem")
    print("3 - Realizar análise da carteira")
    print("4 - Imprimir relatório da carteira")
    print("5 - Sair")
    opcao_menu_principal = int(input("Digite a opção desejada: "))
    if opcao_menu_principal == 5:
        print("")
        print("Agradecemos pela preferência na utilização de nossos serviços! Até a próxima!")
        menu_principal = False
    elif opcao_menu_principal == 4:
        pass
    elif opcao_menu_principal == 3:
        pass
    elif opcao_menu_principal == 2:
        pass
    elif opcao_menu_principal == 1:
        os.system('cls')
        print("Menu Cliente")
        print("1 - Cadastrar Cliente")
        print("2 - Alterar Cliente")
        print("3 - Buscar Cliente")
        print("4 - Deletar Cliente")
        print("5 - Listar Clientes")
        print("6 - Voltar ao menu anterior")
        opcao_menu_cliente = int(input("Digite a opção desejada: "))
        while opcao_menu_cliente < 6:
            if opcao_menu_cliente == 1:
                os.system('cls')

                print("Cadastro de Cliente")
                cliente_dicionario = {
                    "Nome": input("Digite o Nome do Cliente: "),
                    "CPF": valida_cpf(input("Digite o CPF: ")),
                    "RG": valida_rg(input("Digite o RG: (xx.xxx.xxx-x) ")),
                    "Nascimento": valida_data_nascimento(),
                    "Endereco": busca_cep(input("Digite o CEP: ")),
                    "Numero": input("Digite o número da residência: "),
                    "Complemento": input("Digite o complemento (apto, sobrado, referência): ")
                }
                print(cliente_dicionario)
                insert_banco_dados(cliente_dicionario)
                os.system('cls')
                print(f"Cliente com CPF ", cliente_dicionario["CPF"], " cadastrado com sucesso!\n")
                opcao_menu_cliente = 6

            elif opcao_menu_cliente == 2:
                print("")
                print("Atualização de Cliente")
                cliente_cpf = input("CPF: ")
                update_banco_dados(cliente_cpf)
                input("Pressione Enter para retornar ao menu principal...")
                opcao_menu_cliente = 6

            elif opcao_menu_cliente == 3:
                print("")
                print("Busca de Cadastro de Cliente")
                cliente_cpf = input("CPF: ")
                select_banco_dados(cliente_cpf)
                input("Pressione Enter para retornar ao menu principal...")
                opcao_menu_cliente = 6

            elif opcao_menu_cliente == 4:
                print("")
                print("Remoção de Cliente")
                cliente_cpf = input("CPF: ")
                delete_banco_dados(cliente_cpf)
                input("Pressione Enter para retornar ao menu principal...")
                opcao_menu_cliente = 6

            elif opcao_menu_cliente == 5:
                print("")
                print("Consulta de Dados Cadastrais dos Clientes")
                print(lista_banco_dados())
                input("Pressione Enter para retornar ao menu principal...")
                opcao_menu_cliente = 6
                
    else:
        print("Opção Inválida!")
            

# print("Esta função retornará o valor da ação no ultimo pregão registrado no sistema Yahoo Finance")
# ticker = input("Informe o ticker desejado: ") # input sempre retorna string, transformar com int, float se necessario
# print(type(ticker))
# print("Sistema checando dados da ação", ticker,"via Yahoo Finance........")

# if ticker == 'XOM':
#     print("Não vale pedir a cotação da firma!")
#     exit(0)


# #Criterios de pesquisa na base do Yahoo Finance
# stock = pdr.get_quote_yahoo(symbols='IBM', start=datetime(2000, 1, 1), end=datetime(2012, 1, 1))
# print(ibm['Adj Close'])

# #Chama API Yahoo Finance
# retorno_ticker = pdr.get_data_yahoo(ticker, start="2023/6/30")
# #print(retorno_ticker['Adj Close'])

# print("Última cotação: ")
# print("Data do último negócio: ")

##############################

# import pandas_datareader as pdr
# from datetime import datetime

# ibm = pdr.get_data_yahoo(symbols='IBM', start=datetime(2000, 1, 1), end=datetime(2012, 1, 1))
# print(ibm['Adj Close'])




# #Cod original abaixo
# tickers = ['TSLA', 'MSFT', 'GOOG', 'AAPL']  
# interval = '1d'
# period1 = int(time.mktime(datetime.datetime(2021, 1, 1, 23, 59).timetuple()))
# period2 = int(time.mktime(datetime.datetime(2023, 6, 30, 23, 59).timetuple()))

# xlwriter = pd.ExcelWriter('historical prices.xlsx', engine='openpyxl')
# for ticker in tickers:
#     query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
#     df = pd.read_csv(query_string)
#     df.to_excel(xlwriter, sheet_name=ticker, index=False)

# xlwriter._save()
# 