"""
Exercício 9

Nome: Checando Múltiplos
Objetivo: Receber dois números e exibir se um é múltiplo do outro ou não.
Dificuldade: Principiante

1 - Escreva um programa que receba dois números, {numero1} e {numero2}:
2 - Se o {numero1} for múltiplo do {numero2} exiba na tela: "O número {numero1} é múltiplo do número {numero2}.";
3 - Caso contrário, exiba na tela: "O número {numero1} não é múltiplo do número {numero2}.";
"""

numero1 = int(input("Insira o número 1: "))
numero2 = int(input("Insira o número 2: "))

if (numero1 % numero2 == 0):
	print("O número {} é múltiplo no número {}.".format(numero1, numero2))
else:
	print("O número {} não é múltiplo no número {}.".format(numero1, numero2))

