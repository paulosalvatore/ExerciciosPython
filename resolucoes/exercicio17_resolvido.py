"""
Exercício 17

Nome: Par ou Ímpar: Funções
Objetivo: Escrever uma função chamada numero_par que recebe um número e torna True caso ele seja par ou False caso seja ímpar
Dificuldade: Principiante

1 - Crie uma função chamada 'numero_par(numero)' que receba um número como argumento e retorne True caso ele seja par ou False caso seja ímpar.
2 - O número checado deve ser digitado pelo usuário.
"""

# Resolução

# Exitem duas maneiras de resolver esse exercício, utilizando if/else dentro e fora da função (como utilizado no exercício 5) ou utilizando apenas um if/else fora da função

# Pegaremos o número digitado antes de declarar a funções pois será utilizado em comum para ambas as resoluções.

numero_digitado = int(input("Digite um número: "))

# Resolução 1
# Na primeira resolução criamos a função para checar número par e fazemos uma checagem if/else para retornar um booleano indicando se o número é par ou não.


def numero_par_resolucao1(numero):
	if numero % 2 == 0:
		return True
	else:
		return False

if numero_par_resolucao1(numero_digitado):
	print("O número {} é par.".format(numero_digitado))
else:
	print("O número {} é ímpar.".format(numero_digitado))


# Resolução 2
# Na segunda resolução economizamos um pouco e retornamos direto o booleano que é resultado da comparação entre 'numero % 2' e 0, pois sabemos que quando utilizamos um sinal de comparação (no caso, ==), o retorno é sempre um booleano, que posteriormente será utilizado no if/else que estão fora da função.
# O restante é igual, utilizaremos a mesma lógica, apenas alterando o nome da função


def numero_par_resolucao2(numero):
	return numero % 2 == 0

if numero_par_resolucao2(numero_digitado):
	print("O número {} é par.".format(numero_digitado))
else:
	print("O número {} é ímpar.".format(numero_digitado))
