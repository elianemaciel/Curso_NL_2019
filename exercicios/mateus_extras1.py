def multString(valor):
    print(valor*2)

#multString("Hi")    # output -> HiHi
#multString(2)       # output -> 4 


def stringSplosion(string):
   result = ' '
   for i in range(len(string)):
       result = result + string[:i + 1]
   print(result)

#stringSplosion("Code")	# output -> CCoCodCode

