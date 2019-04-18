#!/usr/bin/python
# -*- coding: utf-8 -*-
from historico import Historico
from datetime import datetime


class Conta(object):

    """
    """

    def __init__(self, numero, titular, saldo, limite):

        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.listaHist = []

    def deposita(self, valor):
        data = datetime.strftime(datetime.today(), "%d/%m/%Y")
        histDep = Historico("Deposito", data, valor)
        self.listaHist.append(histDep)

        self.saldo = self.saldo + valor
        print("Voce depositou: {}".format(valor))

    def saca(self, valor):
        data = datetime.strftime(datetime.today(), "%d/%m/%Y")
        histSac = Historico("Saque", data, valor)
        self.listaHist.append(histSac)

        validacao = valor - self.saldo
        if validacao > (self.limite):
           print("Impossivel efetuar o saque, limite excedido!")
        else:
            self.saldo = self.saldo - valor
            print("Voce sacou: {}".format(valor))

    def extrato(self):

        print("Numero da conta: {}\nSaldo: R${}".format(self.numero, self.saldo))
        print("Titular: {} {}\nCPF: {}".format(self.titular.nome, self.titular.sobrenome, self.titular.cpf))
