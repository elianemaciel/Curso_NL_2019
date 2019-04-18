class Conta(object):

    '''Classe da conta'''

    def __init__(self,numero,titular,saldo,limite):
        '''Construtor'''
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self,valor):
        '''Metodo deposita'''
        self.saldo += valor

    def saca(self,valor):
        '''Metodo Saca'''
        self.saldo -= valor

    def extrato(self):
        '''Metodo extrato'''
        print("Numero da Conta: {}".format(self.numero))
        print("Saldo:R${}".format(self.saldo))
        print("Dados do Cliente: {}".format(self.titular.mostrarDados()))

    def mostrarConta(self):
        return "Número: {}, Titular: {}, Saldo: {}, Limite: {}".format(self.numero,self.titular,self.saldo, self.limite)
