from historico import Historico
from datetime import datetime


class Conta(object):

    '''Classe da conta'''

    def __init__(self,numero,titular,saldo,limite,dataabertura):
        '''Construtor conta'''

        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.dataabertura = dataabertura
        self.listahistorico = []

    def deposita(self,valor):
        '''Metodo deposita'''

        self.saldo += valor
        self.listahistorico.append(Historico('Deposito',datetime.today(),valor))

    def saca(self,valor):
        '''Metodo Saca'''

        self.saldo -= valor
        self.listahistorico.append(Historico('Saque',datetime.today(),valor))

    def extrato(self):
        '''Metodo extrato'''

        print("Numero da Conta: {}".format(self.numero))
        print("Saldo:R${}".format(self.saldo))
        print("Data de abertura da conta {}".format(self.dataabertura.mostrarData()))
        print("Dados do Cliente: {}".format(self.titular.mostrarDados()))

    def mostrarConta(self):
        '''Metodo para mostrar conta'''

        return "Número: {}, Titular: {}, Saldo: {}, Limite: {}".format(self.numero,self.titular,self.saldo, self.limite)

    def mostrarListaHistorico(self):
        '''Metodo para mostrar histórico'''

        for i in self.listahistorico:
            print(i.mostrarHistorico())
