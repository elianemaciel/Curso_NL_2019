



def fizzBuzz():
  
  numero= int(input("Digite um numero: "))
  resultado = ""

  if numero % 3 == 0 and numero != 0:
    resultado += "Fizz"
  if numero % 5 == 0 and numero != 0:
    resultado += "Buzz"
  if numero < 0:
    resultado = "Número inválido"
  if resultado =="":
    print(numero)  
   
  print(resultado)

  
  
  
fizzBuzz()