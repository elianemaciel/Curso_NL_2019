class Cliente(object):

    def __init__(self,nome,sobrenome,cpf):
        '''Construtor'''
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf =cpf

    def __repr__(self):
        return "Nome: {}, Sobrenome: {}, Cpf: {}".format(self.nome,self.sobrenome,self.cpf)
