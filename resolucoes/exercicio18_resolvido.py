"""
Exercício 18

Nome: Praticando: Funções Matemáticas
Objetivo: Escrever diversas funções que utilizem as funções matemáticas como base para trabalhar com números e praticar a formatação de números e strings.
Dificuldade: Principiante

1 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_maior_valor' utilizando o método '*args' e retorne o maior deles utilizando a função max()

2 - Peça para o usuário digitar 3 números, envie-os para uma função chamada 'pegar_menor_valor' utilizando o método '*args' e retorne o menor deles utilizando a função min()

3 - Peça para o usuário digitar 3 números positivos e 3 números negativos, extraia o módulo (versão positiva) de cada número utilizando a função abs() e exiba na tela o maior e o menor número (utilize as funções criadas anteriormente no exercício 1 e 2).

4 - Declare uma função que recebe um número e o formata de acordo com o tipo de sua variável (utilize a função type())
- Se a variável for um float, formate-a como moeda, exemplo:
- Entra a variável float 20.0 e exibe na tela R$ 20,00. Regra de formatação: {:.2f}, onde 2 representa o número e casas decimais.
- Se a variável for um int, formate-a deixando com pelo menos 5 dígitos (colocando zeros na frente). Regra de formatação: {:02d}, onde 2 representa o número de dígitos.
- Se a variável for uma string, formata-a para que utilize 10 espaços adicionais à esquerda. Regra de formatação: {:>1}, onde 1 representa o número de espaços que irá utilizar.
- Caso a variável não seja nenhuma dessas, exiba a mensagem "Esse tipo de variável não está mapeado."
"""

# Resolução

# Funções em comum para todos os exercícios


def solicitar_int():
	return int(input("Digite um número inteiro: "))


def solicitar_int_negativo():
	return int(input("Digite um número inteiro negativo: "))


def solicitar_float():
	return float(input("Digite um número decimal: "))


def solicitar_string():
	return input("Digite uma string: ")


# Exercício 1


def pegar_maior_valor(*numeros):
	return max(numeros)

numero1_ex1 = solicitar_int()
numero2_ex1 = solicitar_int()
numero3_ex1 = solicitar_int()

maior_valor = pegar_maior_valor(numero1_ex1, numero2_ex1, numero3_ex1)

print("O maior número entre os números ({}, {}, {}) é: {}.".format(numero1_ex1, numero2_ex1, numero3_ex1, maior_valor))


def pegar_menor_valor(*numeros):
	return min(numeros)


# Exercício 2


def pegar_menor_valor(*numeros):
	return min(numeros)

numero1_ex2 = solicitar_int()
numero2_ex2 = solicitar_int()
numero3_ex2 = solicitar_int()

menor_valor = pegar_menor_valor(numero1_ex2, numero2_ex2, numero3_ex2)

print("O menor número entre os números ({}, {}, {}) é: {}.".format(numero1_ex2, numero2_ex2, numero3_ex2, menor_valor))


# Exercício 3


def pegar_menor_valor(*numeros):
	return min(numeros)

numero_positivo1_ex3 = solicitar_int()
numero_positivo2_ex3 = solicitar_int()
numero_positivo3_ex3 = solicitar_int()

numero_negativo1_ex3 = solicitar_int_negativo()
numero_negativo2_ex3 = solicitar_int_negativo()
numero_negativo3_ex3 = solicitar_int_negativo()

modulo_numero_negativo1_ex3 = abs(numero_negativo1_ex3)
modulo_numero_negativo2_ex3 = abs(numero_negativo2_ex3)
modulo_numero_negativo3_ex3 = abs(numero_negativo3_ex3)

menor_valor = pegar_menor_valor(
	numero_positivo1_ex3,
	numero_positivo2_ex3,
	numero_positivo3_ex3,
	modulo_numero_negativo1_ex3,
	modulo_numero_negativo2_ex3,
	modulo_numero_negativo3_ex3
)

maior_valor = pegar_maior_valor(
	numero_positivo1_ex3,
	numero_positivo2_ex3,
	numero_positivo3_ex3,
	modulo_numero_negativo1_ex3,
	modulo_numero_negativo2_ex3,
	modulo_numero_negativo3_ex3
)

print(
	"Entre os números ({}, {}, {}, {}, {}, {}) o maior é {} e o menor é {}."
	.format(
		numero_positivo1_ex3,
		numero_positivo2_ex3,
		numero_positivo3_ex3,
		modulo_numero_negativo1_ex3,
		modulo_numero_negativo2_ex3,
		modulo_numero_negativo3_ex3,
		maior_valor,
		menor_valor
	)
)


# Exercício 4


def checar_tipo_variavel(variavel):
	tipo = type(variavel)

	if tipo == int:
		print("Variável formatada: {:05d}".format(variavel))
	elif tipo == float:
		print("Variável formatada: {:.2f}".format(variavel))
	elif tipo == str:
		print("Variável formatada: {:>10}".format(variavel))
	else:
		print("Esse tipo de variável não está mapeado.")

int_ex4 = solicitar_int()
float_ex4 = solicitar_float()
string_ex4 = solicitar_string()
booleano = True

checar_tipo_variavel(int_ex4)
checar_tipo_variavel(float_ex4)
checar_tipo_variavel(string_ex4)
checar_tipo_variavel(booleano)
