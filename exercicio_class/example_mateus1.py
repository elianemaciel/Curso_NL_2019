class User(object):
    """
    Uma classe bem simples
    """
    def __init__(self, name):
        """
        Inicializa a classe atribuindo um nome
        """
        self.name = name

def set_password(self, password):
    """
    Troca a senha
    """
    self.password = password

User.set_password = set_password

user = User("Joca")
User.name = "Maicão"

print('Classe orignal', dir(User))
