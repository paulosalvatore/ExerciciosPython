"""
Exercício 21

Nome: Números repetidos
Objetivo: Criar uma lista com alguns números e detectar números repetidos dentro da lista.
Dificuldade: Avançado

1 - Crie uma lista com 20 números quaisquer (certifique-se de que alguns números são repetidos). Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.
2 - Exiba a quantidade de elementos que a lista possui.
3 - Varra todos os números da lista utilizando o for e exiba na tela apenas os números repetidos. Certifique-se de que cada número repetido apareça apenas uma vez.
4 - Declare uma nova lista e insira 20 números (de 1 a 30) de forma aleatória utilizando a biblioteca random, com o método random.randint(inicio, limite). Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela. Consulte a documentação da biblioteca em caso de dúvidas.
5 - Pegue o código de varredura da lista com o for declarado no item 2 e coloque-o em uma função chamada 'detectar_numeros_repetidos(lista)' que recebe um argumento referente a lista de números e retorna apenas os números repetidos. Execute a função declarada no item 5 para a lista de números criada no item 1 e exiba-a na tela.
6 - Execute a função declarada no item 5 para a lista de números criada no item 4.
7 - Crie uma função que receba uma lista de números e exiba na tela a quantidade de vezes que o número aparece repetido. Exiba a mensagem apenas para números repetidos e uma só vez por número. Dica: utilize o método 'lista.count(elemento)'.
8 - Crie uma função que receba uma lista de números e retorne um dicionário para cada número, onde a chave do dicionário é o número em questão e o valor do dicionário é a quantidade de vezes que o número se repete. Utilize o método 'lista.count(elemento)'. Se o item não se repetir, exiba a mensagem "O número X não se repete.", caso contrário, exiba a mensagem "O número X se repete Y vezes.".
9 - Faça a mesma coisa que no item 9, porém, em vez de utilizar o método 'count()', faça a checagem para saber se o item em questão está no dicionário utilizando a checagem do método 'dicionário.get(chave)'. Caso a checagem seja negativa (o dicionário ainda não possui o numero) adicione-o no dicionário utilizando 'dicionario[numero] = 1'. Caso a checagem seja positiva, atribua um valor adicional à posição do dicionário utilizando: 'dicionario[numero] = dicionario[numero] + 1'.
10 - Crie uma função que insere 20 números aleatórios (de 1 a 30) em uma lista certificando de que NENHUM número é repetido. Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.
"""

# Resolução


# Item 1
print("Item 1")
print("1 - Crie uma lista com 20 números quaisquer (certifique-se de que alguns números são repetidos). Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.")


lista = [9, 1, 2, 2, 3, 3, 4, 5, 7, 7, 9, 11, 13, 9, 4, 3, 7, 1, 6, 8]
lista.sort()


# Item 2
print("\nItem 2")
print("2 - Exiba a quantidade de elementos que a lista possui.")


print("A lista {} possui {} elementos.".format(lista, len(lista)))


# Item 3
print("\nItem 3")
print("3 - Varra todos os números da lista utilizando o for e exiba na tela apenas os números repetidos. Certifique-se de que cada número repetido apareça apenas uma vez.")

nova_lista = []

for numero in lista:
	if lista.count(numero) > 1 and nova_lista.count(numero) == 0:
		print("O número {} está repetido.".format(numero))
		nova_lista.append(numero)


# Item 4
print("\nItem 4")
print("4 - Declare uma nova lista e insira 20 números (de 1 a 30) de forma aleatória utilizando a biblioteca random, com o método random.randint(inicio, limite). Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela. Consulte a documentação da biblioteca em caso de dúvidas.")


from random import randint

lista_aleatoria = []

for numero in range(20):
	lista_aleatoria.append(randint(1, 30))

lista_aleatoria.sort()

print("Lista com números aleatórios: {}.".format(lista_aleatoria))


# Item 5
print("\nItem 5")
print("5 - Pegue o código de varredura da lista com o for declarado no item 2 e coloque-o em uma função chamada 'detectar_numeros_repetidos(lista)' que recebe um argumento referente a lista de números e retorna apenas os números repetidos. Exiba a lista na tela.")


def detectar_numeros_repetidos(lista_recebida):
	nova_lista = []

	for numero in lista_recebida:
		if lista_recebida.count(numero) > 1 and nova_lista.count(numero) == 0:
			nova_lista.append(numero)

	return nova_lista


print("A lista {} criada no item 1 possui os seguintes números repetidos: {}".format(lista, detectar_numeros_repetidos(lista)))


# Item 6
print("\nItem 6")
print("6 - Execute a função declarada no item 5 para a lista de números criada no item 4.")

print("A lista {} criada no item 4 possui os seguintes números repetidos: {}".format(lista_aleatoria, detectar_numeros_repetidos(lista_aleatoria)))


# Item 7
print("\nItem 7")
print("7 - Crie uma função que receba uma lista de números e exiba na tela a quantidade de vezes que o número aparece repetido. Exiba a mensagem apenas para números repetidos e uma só vez por número. Dica: utilize o método 'lista.count(elemento)'.")


def exibir_quantidade_repeticao(lista_recebida):
	print("Exibir Quantidade de Repetição da lista {}.".format(lista_recebida))

	numeros_exibidos = []

	for numero in lista_recebida:
		if numeros_exibidos.count(numero) == 0:
			quantidade_repeticao = lista_recebida.count(numero)

			numeros_exibidos.append(numero)

			if quantidade_repeticao > 1:
				print("O número {} aparece {} vezes na lista.".format(numero, quantidade_repeticao))


exibir_quantidade_repeticao(lista)


# Item 8
print("\nItem 8")
print("8 - Crie uma função que receba uma lista de números e retorne um dicionário para cada número, onde a chave do dicionário é o número em questão e o valor do dicionário é a quantidade de vezes que o número se repete. Utilize o método 'lista.count(elemento)'. Se o item não se repetir, exiba a mensagem \"O número X não se repete.\", caso contrário, exiba a mensagem \"O número X se repete Y vezes.\".")


def detectar_quantidade_repeticao(lista_recebida):
	dicionario = {}

	for numero in lista_recebida:
		if not dicionario.get(numero):
			dicionario[numero] = lista_recebida.count(numero)

	return dicionario


lista_numeros_quantidade_repeticao = detectar_quantidade_repeticao(lista_aleatoria)
for numero in lista_numeros_quantidade_repeticao:
	quantidade_repeticao = lista_numeros_quantidade_repeticao[numero]

	if quantidade_repeticao == 1:
		print("O número {} não está repetido.".format(numero))
	else:
		print("O número {} está repetido {} vezes.".format(numero, quantidade_repeticao))


# Item 9
print("\nItem 9")
print("9 - Faça a mesma coisa que no item 9, porém, em vez de utilizar o método 'count()', faça a checagem para saber se o item em questão está no dicionário utilizando a checagem do método 'dicionário.get(chave)'. Caso a checagem seja negativa (o dicionário ainda não possui o numero) adicione-o no dicionário utilizando 'dicionario[numero] = 1'. Caso a checagem seja positiva, atribua um valor adicional à posição do dicionário utilizando: 'dicionario[numero] = dicionario[numero] + 1'.")


def detectar_quantidade_repeticao(lista_recebida):
	dicionario = {}

	for numero in lista_recebida:
		if not dicionario.get(numero):
			dicionario[numero] = 1
		else:
			dicionario[numero] = dicionario[numero] + 1

	return dicionario


lista_numeros_quantidade_repeticao = detectar_quantidade_repeticao(lista_aleatoria)
for numero in lista_numeros_quantidade_repeticao:
	quantidade_repeticao = lista_numeros_quantidade_repeticao[numero]

	if quantidade_repeticao == 1:
		print("O número {} não está repetido.".format(numero))
	else:
		print("O número {} está repetido {} vezes.".format(numero, quantidade_repeticao))


# Item 10
print("\nItem 10")
print("10 - Crie uma função que insere 20 números aleatórios (de 1 a 30) em uma lista certificando de que NENHUM número é repetido. Ordene a lista em ordem numérica com o método 'sort()' e exiba-a na tela.")


def criar_lista_aleatoria_sem_repetir():
	lista = []

	while len(lista) < 20:
		numero_aleatorio = randint(1, 30)

		if lista.count(numero_aleatorio) == 0:
			lista.append(numero_aleatorio)

	return lista

lista_aleatoria_item11 = criar_lista_aleatoria_sem_repetir()
lista_aleatoria_item11.sort()

print("A lista gerada com números aleatórios entre 1 e 30, sem repetir nenhum número é: {}.".format(lista_aleatoria_item11))
