class Gerente(object):
    def __init__(self, nome, cpf, salario, senha):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.senha = senha
        self.numeroDeFuncionariosGerenciados = 0
    
    def autentica(self, senha):
        if self.senha == senha:
            print('Acesso Permitido!')
            return True
        else:
            print("Acesso Negado")
            return False