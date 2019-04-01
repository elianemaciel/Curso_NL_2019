# Exercícios

## if, operadores, variáveis
> Dica do exercício: input, print

1. Leia um número e imprima seu dobro​

2. Faça um Programa que peça dois números e imprima o maior deles.​

3. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

4. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.

5. Faça um programa que transforme uma temperatura fornecida em Celsius para a correspondente em Fahrenheit. A formula de conversão de Celsius  para Fahrenheit é a seguinte: C = (5/9) * (F – 32).

6. Faça um programa que leia dois valores x e y. O programa deve trocar os  valores lidos,  de  forma  que,  ao  final,  x contenha  o  valor  que  foi  inicialmente  atribuído  em  y,  e  y contenha  o  valor  que  foi  inicialmente  atribuído  a  x. Imprima  os  valores  de  x e  y logo  após  a  leitura,  e  depois  imprima novamente após a troca.

7. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
> Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;

## loop, strings, listas, slicing

8. Leia  uma frase e exiba quantas vogais aparecem na frase

9. Crie uma função que recebe uma lista qualquer e:
- retorne o maior elemento
- retorne a soma dos elementos
- retorne o número de ocorrências do primeiro elemento da lista
- retorne a média dos elementos
- retorne o valor mais próximo da média dos elementos
- retorne a soma dos elementos com valor negativo
- retorne a quantidade de vizinhos iguais

10. Faça uma função que receba duas listas e retorne True se são iguais ou False caso contrário. Duas listas são iguais se possuem os mesmos valores e na mesma ordem.

11. Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira metade.

## tuplas, dicionarios

12. Faça um programa que percorre uma lista com o seguinte formato:
[['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela:
- o total de faltas do campeonato
- o time que fez mais faltas
- o time que fez menos faltas

13. Escreva um programa que conta a quantidade de vogais em um texto e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada.

14. Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O campeão é o que tem a menor média de tempos.

15. Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções: ­
incluir_novo_nome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones. ­
- incluir_telefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você - deve perguntar se a pessoa deseja incluí-­lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome. ­
- excluir_telefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda. ­
- excluir_nome – essa função exclui uma pessoa da agenda. ­
- consultar_telefone – essa função retorna os telefones de uma pessoa na agenda.

## random, datetime, built in, funções

16. (random)Tendo como exemplo estas duas listas:
   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- Escreva um programa que retorne uma lista que contém apenas os elementos comuns entre as listas (sem elementos duplicados). - - Verifique se o seu programa funciona em duas listas de diferentes tamanhos.
**Extras:**
- Gerar aleatoriamente duas listas para testar isso.
- Escreva isso em uma linha de Python

17. (built in) Digamos que você tenha uma lista em uma variável: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Em apenas uma linha, faça uma nova lista que tenha apenas os elementos pares.

18. (random) Escreva um gerador de senhas no Python. Seja criativo com a forma como você gera senhas - senhas fortes têm uma mistura de letras minúsculas, letras maiúsculas, números e símbolos. As senhas devem ser aleatórias, gerando uma nova senha sempre que o usuário solicite uma nova senha. Inclua seu código de tempo de execução em um método principal.

19.Faça um programa que escreva em tela o dia da semana do dia atual.
dica do exercício: weekday

20. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
- Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
- O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

21. Faça  um  programa  que  preenche  um  cubo  de  50  x  50  x  50  com  valores  aleatórios entre 0 e 100 e encontre:
- a soma dos valores armazenados no cubo
- o número de ocorrências do valor 90  
- o maior valor armazenado no cubo
- as posições onde aparecem o maior valor encontrado - notar que  aqui o programa possivelmente imprimirá mais de uma posição.

22. Faça um programa que leia n números e mostre-os em ordem decrescente.

## Exceções

23. (usar exceções)Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

24. Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades

25. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
- Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
- Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


26. (dict) Faça um programa que leia 10 conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
