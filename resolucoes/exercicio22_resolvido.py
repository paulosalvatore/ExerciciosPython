"""
Exercício 22

Nome: Fibonacci
Objetivo: Criar um algorítimo que recebe um número de elementos e exibe a sequência de fibonacci correspondente.
Dificuldade: Intermediário

A sequência de Fibonacci é a sequência numérica proposta pelo matemático Leonardo Pisa, mais conhecido como Fibonacci: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Como se pode observar, a sequência inicia em 1 e cada elemento seguinte é dado pela somas dos dois anteriores. Exemplo:
1º elemento: 1
2º elemento: 0 + 1 = 1
3º elemento: 1 + 1 = 2
4º elemento: 1 + 2 = 3
5º elemento: 2 + 3 = 5
6º elemento: 3 + 5 = 8
E assim por diante.

1 - Receba um número digitado pelo usuário.
2 - Construa um algorítimo que seja capaz de mapear a sequência de Fibonacci para o número digitado.
3 - Adicione os números da sequência em uma lista.
4 - Ao final da execução do código, exiba na tela o conteúdo da lista.
"""

# Resolução

numero_elementos = int(input("Digite a quantidade de elementos: "))

lista = [1, 1]
for numero in range(numero_elementos):
	novo_numero = lista[numero] + lista[numero + 1]
	lista.append(novo_numero)

print("A sequência de Fibonacci com {} elementos é:\n{}.".format(numero_elementos, lista))
