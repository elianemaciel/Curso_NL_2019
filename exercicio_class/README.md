# Orientação a Objetos


## Criando uma conta

A conta deve ter os atributos, numero, titular, saldo e limite.
Devemos manipular os dados através das funcionalidades saca() e deposita() e proteger os dados da conta. Pensando no mundo real, ninguém pode modificar o saldo de sua conta quando quiser, a não ser quando vamos fazer um saque ou um depósito. A mesma coisa deve acontecer aqui.

- Criar uma classe para o a conta

- Crie o método construtor para inicializar numero, titular, saldo, limite

### Métodos

- Crie um método *deposita()* que recebe como argumento uma conta e um valor.

- Crie um método saca() que recebe como argumento um valor. Dentro da função subtraia o valor do saldo da conta

- Crie um método extrato(), que imprime o numero e o saldo da conta

>> (Opcional) Acrescente uma documentação para os métodos e utilize a função help() para testá-la.

- Crie uma classe para representar um cliente do nosso banco que deve ter nome, sobrenome e cpf. Instancie uma Conta e passe um cliente como titular da conta. Modifique o método extrato() da classe Conta para imprimir, além do número e o saldo, os dados do cliente. Podemos criar uma Conta sem um Cliente? E um Cliente sem uma Conta?

- Crie uma classe que represente uma data, com dia, mês e ano. Crie um atributo data_abertura na classe Conta. Crie uma nova conta e faça testes no console do Python.

- Crie uma classe Historico que represente o histórico de uma Conta seguindo o exemplo da apostila. Faça testes no console do Python criando algumas contas, fazendo operações e por último mostrando o histórico de transações de uma Conta. Faz sentido criar um objeto do tipo Historico sem uma Conta?
