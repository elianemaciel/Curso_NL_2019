class Cliente(object):

    '''Classe cliente'''

    def __init__(self,nome,sobrenome,cpf):
        '''Construtor cliente'''

        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf =cpf

    def mostrarDados(self):
        '''Metodo para mostrar dados'''

        return "Nome: {}, Sobrenome: {}, Cpf: {}".format(self.nome,self.sobrenome,self.cpf)
