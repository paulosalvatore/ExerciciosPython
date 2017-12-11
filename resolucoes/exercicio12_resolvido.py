"""
Exercício 12

Nome: Praticando Funções
Objetivo: Escrever diversas funções para reaproveitar trechos de código
Dificuldade: Principiante

Escreva um código de modo que exiba o valor do x digitado pelo usuário e que seja
substituído nas funções.
1 - Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).
2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável
de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine
o custo de produção de 100 peças.
3 - Crie uma função que receba 2 números e retorne o maior valor.
4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.
5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da
soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções
com números digitados pelo usuário.
6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1.
Qual é o valor da função composta g(f(3))? Depois crie um código que retorne o valor da
soma das duas funções com números digitados pelo usuário.
7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.
Exiba 10 números sorteados utilizando a mesma função criada.
Números aleatórios: random.randint(inicio, fim)
"""

# Resolução


def solicitarNumero(mensagem):
	numero = int(input(mensagem))
	return numero


# Item 1: Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).
print("Item 1: Sendo f(x) = 3x - 2 determine o valor de f(5) + f(0).")


def calcularF_ex1(x):
	return 3 * x - 2

numero1_ex1 = solicitarNumero("Insira o primeiro número da função: ")
numero2_ex1 = solicitarNumero("Insira o segundo número da função: ")

resultadoF1_ex1 = calcularF_ex1(numero1_ex1)
resultadoF2_ex1 = calcularF_ex1(numero2_ex1)

resultado_ex1 = resultadoF1_ex1 + resultadoF2_ex1

print("O resultado de f({}) + f({}) é {}.".format(numero1_ex1, numero2_ex1, resultado_ex1))


# Item 2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável
# de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine
# o custo de produção de 100 peças.
print("\nItem 2 - Na produção de peças, uma fábrica tem um custo fixo de R$ 30,00 mais um custo variável")
print("de R$ 2,00 por unidade produzida. Sendo x o número de peças unitárias produzidas, determine")
print("o custo de produção de 100 peças.")

custoFixo = 30
custoVariavel = 2


def calcularPecas(pecas):
	return custoFixo + (pecas * custoVariavel)


pecas = solicitarNumero("Digite o número de peças para calcular o custo de produção: ")

print("O custo da produção de {} peças é de R$ {:.2f}.".format(pecas, calcularPecas(pecas)))


# Item 3 - Crie uma função que receba 2 números e retorne o maior valor.
print("\nItem 3 - Crie uma função que receba 2 números e retorne o maior valor.")


def checarMaiorValor(a, b):
	if a > b:
		return a
	else:
		return b

a = solicitarNumero("Insira o valor de A: ")
b = solicitarNumero("Insira o valor de B: ")
maior = checarMaiorValor(a, b)
print("Entre A ({}) e B ({}), o maior valor é ({}).".format(a, b, maior))


# Item 4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.
print("\nItem 4 - Crie uma função que receba 3 números e retorne o maior valor, use a função da questão 3.")

a = solicitarNumero("Insira o valor de A: ")
b = solicitarNumero("Insira o valor de B: ")
c = solicitarNumero("Insira o valor de C: ")
maior = checarMaiorValor(a, b)
maior = checarMaiorValor(maior, c)
print("Entre A ({}), B ({}) e C ({}), o maior valor é ({}).".format(a, b, c, maior))


# Item 5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da
# soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções
# com números digitados pelo usuário.
print("\nItem 5 - Dadas as funções f(x) = x – 5 e g(x) = 3x + 1, crie um código que retorne o valor da")
print("soma de f(9) + g(2). Depois crie um código que retorne o valor da soma das duas funções")
print("com números digitados pelo usuário.")


def calcularFuncao1_ex5(x):
	return x - 5


def calcularFuncao2_ex5(x):
	return (3 * x) - 1


numero1 = solicitarNumero("Insira o valor para a função 'f(x) = x – 5': ")
numero2 = solicitarNumero("Insira o valor para a função 'g(x) = 3x + 1': ")

resultado = calcularFuncao1_ex5(numero1) + calcularFuncao2_ex5(numero2)

print("O valor da soma de f({}) e g({}) é '{}'.".format(numero1, numero2, resultado))


# Item 6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1.
print("\nItem 6 - Considere as seguintes funções: f(x) = x - 4 e g(x) = 5x + 1.")
print("Qual é o valor da função composta g(f(3))? Depois crie um código que retorne o valor da")
print("soma das duas funções com números digitados pelo usuário.")


def calcularFuncao1_ex6(x):
	return x - 4


def calcularFuncao2_ex6(x):
	return (5 * x) + 1


numero = solicitarNumero("Insira o valor de X: ")

resultado = calcularFuncao2_ex6(calcularFuncao1_ex6(numero))

print("O resultado de g(f({})) é '{}'.".format(numero, resultado))


# Item 7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.
# Exiba 10 números sorteados utilizando a mesma função criada.
# Números aleatórios: random.randint(inicio, fim)
print("\nItem 7 - Crie uma função chamada dado() que retorna, através de sorteio, um número de 1 até 6.")
print("Exiba 10 números sorteados utilizando a mesma função criada.")
print("Números aleatórios: random.randint(inicio, fim)")

import random


def dado():
	return random.randint(1, 6)


print("Número 1 sorteado no dado: '{}'.".format(dado()))
print("Número 2 sorteado no dado: '{}'.".format(dado()))
print("Número 3 sorteado no dado: '{}'.".format(dado()))
print("Número 4 sorteado no dado: '{}'.".format(dado()))
print("Número 5 sorteado no dado: '{}'.".format(dado()))
print("Número 6 sorteado no dado: '{}'.".format(dado()))
print("Número 7 sorteado no dado: '{}'.".format(dado()))
print("Número 8 sorteado no dado: '{}'.".format(dado()))
print("Número 9 sorteado no dado: '{}'.".format(dado()))
print("Número 10 sorteado no dado: '{}'.".format(dado()))
