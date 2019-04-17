from datetime import datetime
import traceback

def validarData(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except:
        return False

def diaSemana(data):
    try:
        dias = ['Segunda-Feira',
                'Terça-Feira',
                'Quarta-Feira',
                'Quinta-Feira',
                'Sexta',
                'Sábado',
                'Domingo']

        print(dias[data.weekday()])
    except e:
        print(e)

def verificarData(data):
    try:
        data_new = datetime.strptime(data, '%d/%m/%Y')
        return data_new
    except:
        try:
            data_new = datetime.strptime(data, '%d-%m-%Y')
            return data_new
        except:
            try:
                data_new = datetime.strptime(data, '%d%m%Y')
                return data_new
            except e:
                print(e)


def main():
    data = str(input('Informe uma data: '))
    print(validarData(data))
    data = datetime.today()
    print(diaSemana(data))
    data = str(input('Informe uma data: '))
    print(verificarData(data))

main()
