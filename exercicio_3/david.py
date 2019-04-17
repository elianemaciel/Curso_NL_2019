 from datetime import datetime



 def dataValida(dataescrita):
     try:
         datetime.strptime(dataescrita, "%d/%m/%Y")
         return True
     except:
         return False



 def diaDaSemana(hoje):
     weekday_name = ["SEGUNDA","TERCA","QUARTA","QUINTA","SEXTA","SABADO","DOMINGO"]
     return weekday_name[hoje.weekday()]

 def formatoValido(dataescrita):
     try:
         valido1 = datetime.strptime(dataescrita, "%d/%m/%Y")
         return valido1
     except:
         try:
             valido1 = datetime.strptime(dataescrita, "%d-%m-%Y")
             return valido1
         except:
             try:
                 valido1 = datetime.strptime(dataescrita, "%d%m%Y")
                 return valido1
             except falso:
                 print(falso)



 def main():
     dataescrita = input("Digite a data: ")

     hoje = datetime.today()
     semana = diaDaSemana(hoje)
     print(semana)
     formato = formatoValido(dataescrita)
     print(formato)
     data = dataValida(dataescrita)
     print(data)

 main()
