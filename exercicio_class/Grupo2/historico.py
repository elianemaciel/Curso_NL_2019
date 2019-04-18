from datetime import datetime


class Historico(object):
    '''Classe hitorico'''

    def __init__(self,tipoMovimento,data,valor):
        '''Construtor historico'''

        self.tipoMovimento = tipoMovimento
        self.data = datetime.strftime(data,'%d/%m/%Y')
        self.valor = valor


    def mostrarHistorico(self):
        '''Metodo mostrar historico'''

        return "Tipo de Movimento: {}, Data: {}, Valor: {}".format(self.tipoMovimento,self.data,self.valor)
