class Pendrive(object):
    def __init__(self, tamanho, interface='2.0'):
        self.tamanho = tamanho
        self.interface = interface

class MP3Player(Pendrive):
    def __init__(self, tamanho, interface='2.0', turner=False):
        self.turner = turner
        Pendrive.__init__(self, tamanho, interface)
