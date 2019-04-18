class Cell(object):
    """
    Classe para cédulas de planilha
    """

    def __init__(self, formula='""', format='%s'):
        """
        Inicializa a célula
        """
        self.formula = formula
        self.format = format

    def __repr__(self):
        """
        Retorna a representação em string da cédula
        """
        return self.format % eval(self.formula)

print(Cell('123**2'))                       # set formula
print(Cell('23*2+2'))                       # set formula
print(Cell('abs(-1.45 / 0.3)', '%2.3f'))    # set formula - set format