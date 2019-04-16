def multString(valor, multiplicador):
   return valor*multiplicador

#result = multString("Hi", 2)    # output -> HiHi
#result = multString(2, 2)       # output -> 4 

def stringSplosion(string):
   result = ' '
   for i in range(len(string)):
       result = result + string[:i + 1]
   return result

#result = stringSplosion("Code")	# output -> CCoCodCode

nums = [1,2,3,4,5,6,7,8,9,9,9]
def arrayCount9(lista):
   return (lista.count(9))

#result = arrayCount9(nums)   # output -> 3

def arrayFront9(lista):
   for i in range(4):
      if lista[i] == 9:
         return True
      return False

#result = arrayFront9(nums)   # output -> False

def helloName(nome):
   return (f'Hello {nome}!')

#result = helloName("Joca") # output -> Hello Joca!

def makeTag(tag, string):
 