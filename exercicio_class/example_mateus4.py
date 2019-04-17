class Projetil(object):
    def __init__(self, alcance, tempo):
        self.alcance = alcance
        self.tempo = tempo
    
    @property
    def velocidade(self):
        return self.alcance / self.tempo

calc = Projetil(alcance=1000, tempo=60)

print(calc.velocidade)