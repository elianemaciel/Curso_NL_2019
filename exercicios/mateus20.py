from random import randint

a = [randint(0, 100) for i in range(randint(0, 100))]
b = [randint(0, 100) for i in range(randint(0, 100))]

a = set(a)
b = set(b)

for i in b:
    if i in a:
     print ("{} tem na lista A e B".format(i))
