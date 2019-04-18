""" David, Jaqueline, Gabriel, Junior"""

from conta import Conta
from cliente import Cliente
from data import Data
from datetime import datetime
from historico import Historico

def Main():
    '''Metodo main'''

    contaCriada = None
    resposta = "S"
    while resposta =="S":
        print("DIGITE 1 PARA CADASTRAR CLIENTE")
        print("DIGITE 2 PARA SACAR")
        print("DIGITE 3 PARA DEPOSITAR")
        print("DIGITE 4 PARA EXTRATO")
        print('DIGITE 5 PARA MOSTRAR HISTORICO')
        print('DIGITE 0 PARA SAIR')
        entrada = int(input("ESCOLHA A FUNÇÃO: "))

        if entrada == 1:
            '''Entrada 1, entrada do cliente'''
            a= input("Nome:")
            b= input("Sobrenome:")
            c= input("CPF:")
            d= Cliente(nome=a, sobrenome=b,cpf=c)
            s= int(input("Número da conta:"))
            x= int(input("Saldo inicial da conta:"))
            y= int(input("Limite da conta:"))
            z= Data()
            contaCriada = Conta(numero=s, titular=d, saldo=x, limite=y, dataabertura= z)

        if entrada == 2:
            '''Entrada 2, entrada para o saque'''
            valorSaque = int(input('valor do saque: '))
            contaCriada.saca(valorSaque)


        if entrada == 3:
            '''Entrada 3, para depositar'''
            valorDeposito = int(input("Valor do Deposito: "))
            contaCriada.deposita(valorDeposito)

        if entrada == 4:
            '''Entrada 4, para ver o extrato'''
            contaCriada.extrato()

        if entrada == 5:
            '''Entrada 5, para mostrar o historico'''
            contaCriada.mostrarListaHistorico()

        resposta = str(input("DESEJA FAZER NOVA TRANSAÇÃO?[S/N] ")).upper()

Main()
