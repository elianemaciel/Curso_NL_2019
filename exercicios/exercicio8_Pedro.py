#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1=float(input("digite a primeira nota: "))
n2=float(input("digite a segunda nota: "))
media=(n1+n2)/2
if media>=7 and media <10:
    print("APROVADO")
if media<7:
    print("REPROVADO")
if media==10:
    print("APROVADO COM DISTINCAO")
