"""
Exercício 24

Nome: Data de Nascimento
Objetivo: Criar uma aplicação que receba uma data de nascimento e exiba a quantidade de dias que a pessoa já viveu e o dia da semana que ela nasceu.
Dificuldade: Intermediário

1 - Importe o método 'datetime' da biblioteca 'datetime': from datetime import datetime
2 - Peça para a pessoa digitar a data de nascimento no formato DD/MM/AAAA, exemplo: 27/11/1993;
3 - Quebre o valor digitado utilizando o método split() utilizando a barra '/' como separador;
4 - Confira se na nova lista gerada, o primeiro elemento corresponde ao dia, o segundo ao mês e o terceiro ao ano. Armazene esses valores em variáveis separadas chamadas 'dia', 'mes' e 'ano', respectivamente. Certifique-se de que você converteu os valores digitados em números inteiros utilizado o método int();
5 - Utilizando a biblioteca datetime, crie um novo objeto de data utilizando os valores obtidos;
6 - Crie uma função que recebe um objeto de datetime e retorne o número exato de dias que a pessoa viveu. Utilize: 'data.days';
7 - Exiba o número obtido através da função na tela (o print deve estar fora da função).
8 - Crie uma lista com os dias da semana, onde 0 = Segunda e 6 = Domingo
9 - Exiba na tela o dia da semana em que a pessoa nasceu (por extenso)
"""
