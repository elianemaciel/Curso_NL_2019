import datetime, sys

def main():
    data = input("Digite uma data: ")

    #formatoData(data) # -> testa em formatos DD/MM/YYYY DD-MM-YYYY DDMMYYYY
    validarData(data) # -> testa no formato DD/MM/YYYY
    diaSemana(data)   # -> dia da semana, conforme a função validarData()
    
# formato -> 'DD/MM/YYYY'
def validarData(data):
    try:
        datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except ValueError:
        print("(Função validarData)Erro no formato: {}".format(sys.exc_info()[1]))

def diaSemana(data):
    try:
        dias = ["Segunda - Feira",
                "Terca - Feira",
                "Quarta - Feira",
                "Quinta - Feira",
                "Sexta - Feira",
                "Sábado",
                "Domigo"]

        data = datetime.datetime.strptime(data, '%d/%m/%Y')
        indiceDia = data.weekday()
        return dias[indiceDia]
    except:
        print("(Dia da semana)Erro -> {}".format(sys.exc_info()[1]))

# formato -> 'DD/MM/YYYY' 'DD-MM-YYYY' 'DDMMYYYY'
def formatoData(data):
    try:
        testFormat = datetime.datetime.strptime(data, '%d/%m/%Y')
        return True
    except:    
        try:
            testFormat = datetime.datetime.strptime(data, '%d-%m-%Y')
            return True
        except:
            try:
                testFormat = datetime.datetime.strptime(data, '%d%m%Y')
                return True
            except:
                print("(Formarto Data)Erro no formato: {}".format(sys.exc_info()[1]))
                return True

main()
