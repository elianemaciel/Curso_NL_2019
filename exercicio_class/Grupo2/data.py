from datetime import datetime


class Data():
    '''Classe Data'''

    def __init__(self):
        '''Construtor data'''

        agora= datetime.now()
        self.ano= agora.year
        self.mes = agora.month
        self.dia = agora.day

    def mostrarData(self):
        '''metodo para mostrar data'''

        return "Ano: {}, Mes: {}, Dia: {}".format(self.ano,self.mes,self.dia)
