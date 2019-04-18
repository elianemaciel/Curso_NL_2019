#!/usr/bin/python
# -*- coding: utf-8 -*-
class Historico(object):

    def __init__(self, tipo, data, valor):

        self.tipo = tipo
        self.data = data
        self.valor = valor

    def mostraHist(self):
        print("{}\nDia: {}\nValor: {}".format(self.tipo, self.data, self.valor))   
