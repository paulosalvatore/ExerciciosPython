"""
Exercício 19

Nome: Praticando: Listas/For (Loop)
Objetivo: Praticar a criação e a leitura básica de listas com números e textos.
Dificuldade: Intermediário

1 - Crie uma lista com alguns números inseridos manualmente (não há necessidade do usuário inserí-los).
2 - Crie um for que varra cada elemento da lista e exiba-o no console.
3 - Declare um novo for que exiba apenas os números maiores que 3.
4 - Declare um outro for que exiba apenas os números pares.
5 - Exiba na tela a soma de todos os elementos da lista sem a utilização de funções extras.
6 - Exiba a soma de todos os elementos utilizando a função sum().
7 - Crie uma nova lista a partir de números digitados pelo usuário, faça com que o usuário insira 10 números, porém, utilize o 'for' para isso, em vez de declarar 10 vezes o input de entrada de informação, declare apenas UMA vez e faça com que ele seja executado 10 vezes.
A cada atualização da lista, exiba a quantidade de elementos que ela possui.
8 - Exiba apenas os três primeiros elementos da lista no console.
9 - Exiba apenas os três últimos elementos da lista no console.
10 - Declare uma nova lista vazia chamada 'nomes' e armazene 3 nomes digitados pelo usuário, ordene esses nomes por ordem alfabética e exiba-os na tela, um de cada vez.
"""

# Resolução

# Item 1
print("Item 1")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Item 2
print("Item 2")

for numero in lista:
	print(numero)

# Item 3
print("Item 3")

for numero in lista:
	if numero > 3:
		print(numero)

# Item 4
print("Item 4")

for numero in lista:
	if numero % 2 == 0:
		print(numero)

# Item 5
print("Item 5")

total = 0

for numero in lista:
	total += numero

print("A soma de todos os números da lista é {}.".format(total))

# Item 6
print("Item 6")

print("A soma de todos os números da lista é {}.".format(sum(lista)))

# Item 7
print("Item 7")

lista_numeros_usuario = []

print("A lista possui {} elementos.".format(len(lista_numeros_usuario)))

for numero in range(10):
	numero_digitado = int(input("Digite o {}º número: ".format(numero + 1)))
	lista_numeros_usuario.append(numero_digitado)
	print("A lista possui {} elementos.".format(len(lista_numeros_usuario)))

# Item 8
print("Item 8")

print("Os três primeiros elementos da lista de números digitados pelo usuário são: {}.".format(lista_numeros_usuario[:3]))

# Item 9
print("Item 9")

print("Os três últimos elementos da lista de números digitados pelo usuário são: {}.".format(lista_numeros_usuario[7:10]))

# Item 10
print("Item 10")

lista_nomes = []

for indice in range(3):
	nome = input("Digite o {}º nome: ".format(indice + 1))
	lista_nomes.append(nome)

lista_nomes.sort()

for nome in lista_nomes:
	print(nome)
