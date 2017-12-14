"""
Exercício 20

Nome: Números primos
Objetivo: Criar um for (loop) para detectar se um número é primo ou não.
Dificuldade: Avançado

Os números primos são aqueles números divisíveis APENAS por ele mesmo e por um.
Ele NÃO PODE ser divisível por qualquer número entre esses.
Por exemplo:
2 é primo pois ele é divisível apenas por 1 e por 2.
3 é primo pois ele é divisível apenas por 1 e por 3.
4 não é primo pois ele é divisível por 1, por 2 e por 4.
E assim por diante.

Para checar se um número é primo na programação, precisamos checar se ele é divisível por cada número que está entre ele e 1, para isso, utilizamos o 'for'.

1 - Crie um programa que receba um número digitado pelo usuário e execute um 'for' pelo exato número de vezes do número digitado.
2 - Para cada vez que o 'for' rodar, cheque se o número principal que foi digitado é divisível por aquele número que está no for em questão.
Para saber se um número é divisível pelo outro, saiba que o resto da divisão inteira deve resultar em 0 (zero).
Dica: Crie uma variável chamada 'contador' e para cada vez que um número for divisível pelo outro, acrescente 1 (um) ao valor do contador, se ao final da execução do loop, o contador for igual a 2, significa que o número é primo, caso contrário (3 ou mais) o número NÃO é primo.
Outra dica: Quando o range é utilizado, o for começa a ser executado a partir do índice 0, por tanto, o número que você terá que começar a realizar a divisão é 1.
"""
