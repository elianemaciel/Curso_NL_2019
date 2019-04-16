"""Trabalhando com strings:

multstring: seja uma string s e um inteiro positivo n retorna uma string com n cópias da string original multstring('Hi', 2) -> 'HiHi'
string_splosion: string_splosion('Code') -> 'CCoCodCode', string_splosion('abc') -> 'aababc', string_splosion('ab') -> 'aab'
array_count9: conta quantas vezes aparece o 9 numa lista nums
array_front9: verifica se pelo menos um dos quatro primeiros é nove, array_front9([1, 2, 9, 3, 4]) -> True array_front9([1, 2, 3, 4, 9]) -> False, array_front9([1, 2, 3, 4, 5]) -> False
hello_name: seja uma string name hello_name('Bob') -> 'Hello Bob!'
make_tags: make_tags('i', 'Yay'), 'Yay', make_tags('i', 'Hello'), 'Hello'
I. sem_pontas - seja uma string s de pelo menos dois caracteres retorna uma string sem o primeiro e último caracter - without_end('Hello') -> 'ell'"""

s = input("Escreva algo: ")
n = int(input("Digine um numero inteiro: "))

print(s*n)


print(s[0],s[0],s[1],s[0],s[1],s[2],s)
