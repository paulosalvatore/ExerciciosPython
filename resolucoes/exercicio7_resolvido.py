"""
Exercício 7

Nome: Arredondando para Múltiplos
Objetivo: Receber dois números e arredondar o primeiro número para o número mais próximo do múltiplo do segundo número.
Dificuldade: Principiante

1 - Receba dois números, o primeiro na variável 'numero' e o segundo na variável 'multiplo'.
2 - Arredonde para baixo o valor do primeiro número levando em consideração que o resultado deve ser múltiplo do segundo número.

Exemplo:

Supondo que o primeiro número seja 72 e o segundo número seja 10, o resultado será 70.
Se o primeiro número for 97 e o segundo número for 10, o resultado será 90.
"""

numero = int(input("Insira o primeiro número: "))
multiplo = int(input("Insira o segundo número (multiplo): "))

resultado = numero - (numero % multiplo)

print("O valor arredondado para baixo do número {} para que seja múltiplo de {} é igual a {}.".format(numero, multiplo, resultado))
