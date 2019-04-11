# Programa Talentos NL 2019

Este repositório servirá como guia para os exercícios feitos durante o treinamento de python.

## Submissão dos exercícios

- Nas pastas exercício 1, 2, 3 e 4, tem um exercício este deve ser postado individualmente.
- Na pasta de exercícios, contem varios exercícios. Para cada exercício, deve ser colocado o seu nome e o numero do exercício.
- Desafios: HackerRank <www.hackerrank.com/programa-de-talentos-nl>

Ex: exerc1_eliane.py

# Exercícios

## Operadores, Variáveis, Strings
> Dica do exercício: input, print

1. Leia um número e imprima seu dobro​.

2. Faça um programa que transforme uma temperatura fornecida em Celsius para a correspondente em Fahrenheit. A formula de conversão de Celsius  para Fahrenheit é a seguinte: C = (5/9) * (F – 32).

3. Leia  uma frase e exiba quantas vogais aparecem na frase.

### DESAFIO

- [sWAP cASE](https://www.hackerrank.com/contests/programa-de-talentos-nl/challenges/swap-case)

## Tuplas, Listas, Dicionários

4. Crie um programa que recebe uma lista qualquer e:
- retorne o maior elemento
- retorne a soma dos elementos
- retorne o número de ocorrências do primeiro elemento da lista
- retorne a média dos elementos
- retorne o valor mais próximo da média dos elementos
- retorne a soma dos elementos com valor negativo
- retorne a quantidade de vizinhos iguais

### DESAFIO

- [Lists](https://www.hackerrank.com/contests/programa-de-talentos-nl/challenges/python-lists)

## Condicionais

5. Faça um Programa que peça dois números e imprima o maior deles.​

6. Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

7. Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.

8. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.

9. Faça um programa que leia dois valores x e y. O programa deve trocar os  valores lidos,  de  forma  que,  ao  final,  x contenha  o  valor  que  foi  inicialmente  atribuído  em  y,  e  y contenha  o  valor  que  foi  inicialmente  atribuído  a  x. Imprima  os  valores  de  x e  y logo  após  a  leitura,  e  depois  imprima novamente após a troca.

10. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
> Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;

## DESAFIO

- [Exercicio 4](exercicio_4/README.md)
- [Python If-Else](https://www.hackerrank.com/contests/programa-de-talentos-nl/challenges/py-if-else)

## Laços de Repetição

11. Faça um programa que percorre uma lista com o seguinte formato:
[['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:
- o total de faltas do campeonato
- o time que fez mais faltas
- o time que fez menos faltas

## Funções

12. Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O campeão é o que tem a menor média de tempos.

13. Faça uma função que receba duas listas e retorne True se são iguais ou False caso contrário. Duas listas são iguais se possuem os mesmos valores e na mesma ordem.

14. Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade.

15. Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

16. Implementar uma função que receba uma lista de listas de comprimentos quaisquer e retorne uma lista de uma dimensão.

17. Implementar uma função que receba um dicionário e retorne a soma, a média e a variação dos valores.

18. Escreva uma função que:

- Receba uma frase como parâmetro.
- Retorne uma nova frase com cada palavra com as letras invertidas.

19. Crie uma função que:

- Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão igual) e um booleano (reverso, falso por padrão).
- Retorne dados ordenados pelo item indicado pela chave e em ordem decrescente se reverso for verdadeiro.


## Random, Datetime, Built in, List Comprehensions, Regex

20. (random)Tendo como exemplo estas duas listas:
- a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
- b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- Escreva um programa que retorne uma lista que contém apenas os elementos comuns entre as listas (sem elementos duplicados).
- Verifique se o seu programa funciona em duas listas de diferentes tamanhos.

**Extras:**
- Gerar aleatoriamente duas listas para testar isso.
- Escreva isso em uma linha de Python

21. (built in) Digamos que você tenha uma lista em uma variável: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Em apenas uma linha, faça uma nova lista que tenha apenas os elementos pares.

22. (random) Escreva um gerador de senhas no Python. Seja criativo com a forma como você gera senhas - senhas fortes têm uma mistura de letras minúsculas, letras maiúsculas, números e símbolos. As senhas devem ser aleatórias, gerando uma nova senha sempre que o usuário solicite uma nova senha. Inclua seu código de tempo de execução em um método principal.

23. (datetime)Faça uma função que receba uma data e escreva em tela o dia da semana.
dica do exercício: weekday

24. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

| Média de Aproveitamento | Conceito |
| ----------------------- | --------:|
| Entre 9.0 e 10.0        | A        |
| Entre 7.5 e 9.0         | B        |
| Entre 6.0 e 7.5         | C        |
| Entre 4.0 e 6.0         | D        |
| Entre 4.0 e zero        | E        |

- O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

25. Faça  um  programa  que  preenche  um  cubo  de  50  x  50  x  50  com  valores  aleatórios entre 0 e 100 e encontre:
- a soma dos valores armazenados no cubo
- o número de ocorrências do valor 90  
- o maior valor armazenado no cubo
- as posições onde aparecem o maior valor encontrado - notar que  aqui o programa possivelmente imprimirá mais de uma posição.

26. Implementar um gerador de números primos.

27. Implementar o gerador de números primos como uma expressão (dica: use o módulo itertools).

28. Implementar um gerador que produza tuplas com as cores do padrão RGB (R, G e B variam de 0 a 255) usando xrange() e uma função que produza uma lista com as tuplas RGB usando range(). Compare a performance.

29. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas com os dados (o separador de campo do arquivo é vírgula), eliminando as linhas vazias. Caso ocorra algum problema, imprima uma mensagem de aviso e encerre o programa.


## DESAFIO

- [Exercicio 1](exercicio_1/README.md)
- [Exercicio 2](exercicio_2/README.md)
- [Exercicio 3](exercicio_3/README.md)

## Exceções

30. (usar exceções)Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

31. Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades

32. (dict) Faça um programa que leia 10 conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

33. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções: ­
incluir_novo_nome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones. ­
- incluir_telefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você - deve perguntar se a pessoa deseja incluí-­lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. ­
- excluir_telefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. ­
- excluir_nome – essa função exclui uma pessoa da agenda. ­
- consultar_telefone – essa função retorna os telefones de uma pessoa na agenda.

## Orientação a Objetos

34. Desenvolva uma classe para trabalhar com números complexos, na qual estejam definidos os métodos para realizar as quatro operações básicas com este conjunto numérico. Estas operações são:
- Adição: (a + bi) + (c + di)

35. Crie uma classe que modele um quadrado, com um atributo lado e os métodos: mudar valor do lado, retornar valor do lado e calcular área.

36. Implemente uma classe Carro com as seguintes propriedades:

- Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
- O consumo é especificado no construtor e o nível de combustível inicial é 0.
- Forneça um método mover(km) que receba a distância em quilômetros e reduza o nível de combustível no tanque de gasolina.
- Forneça um método gasolina(), que retorna o nível atual de combustível.
- Forneça um método abastecer(litros), para abastecer o tanque.

37. Implementar uma classe Vetor:

- Com coordenadas x, y e z.
- Que suporte soma, subtração, produto escalar e produto vetorial.
- Que calcule o módulo (valor absoluto) do vetor.

38. Implemente um módulo com:

- Uma classe Ponto, com coordenadas x, y e z.
- Uma classe Linha, com dois pontos A e B, e que calcule o comprimento da linha.
- Uma classe Triangulo, com dois pontos A, B e C, que calcule o comprimento dos lados e a área.


## EXTRAS:

- [Find Angle MBC](https://www.hackerrank.com/contests/programa-de-talentos-nl/challenges/find-angle)
