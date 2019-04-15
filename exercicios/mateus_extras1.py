def multString(valor):
    print(valor*2)

#multString("Hi")    # output -> HiHi
#multString(2)       # output -> 4 


def stringSplosion(string):
    for i in string:
        string += string
        print(i)
        
stringSplosion("Code")
