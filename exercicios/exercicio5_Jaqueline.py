# Faça um Programa que peça dois números e imprima o maior deles.​

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O maior número digitado foi: {}'.format(n1))
elif n2 > n1:
    print('O maior número digitado foi: {}'.format(n2))
else:
    print('Os números digitados são iguais.')
