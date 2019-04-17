#!/usr/bin/python
# -*- coding: utf-8 -*-
class Conta(object):

    """
    """

    def __init__(self, numero, titular, saldo, limite):

        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):

        self.saldo = self.saldo + valor

    def saca(self, valor):
        validacao = valor - self.saldo
        if validacao > (self.limite):
           print("Impossivel efetuar o saque, limite excedido!")
        else:
            self.saldo = self.saldo - valor

    def extrato(self):

        print("Numero da conta: {}\nSaldo: R${}".format(self.numero, self.saldo))
        print("Titular: {} {}\nCPF: {}".format(self.titular.nome, self.titular.sobrenome, self.titular.cpf))
