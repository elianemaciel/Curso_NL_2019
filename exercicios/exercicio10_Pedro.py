l1=float(input("Digite o valor do lado um: "))
l2=float(input("Digite o valor do lado dois: "))
l3=float(input("Digite o valor do lado tres: "))
if (l1+l2)>l3 and (l2+l3)>l1 and (l1+l3)>l2:
    if l1==l2 and l1==l3 and l2==l3:
        print("TRIANGULO EQUILATERO")
    elif l1!=l2 and l1!=l3 and l2!=l3:
        print("TRIANGULO ESCALENO")
    else :
        print("TRIANGULO ISOSCELES")
else :
    print("TRIANGULO NAO FORMADO")
