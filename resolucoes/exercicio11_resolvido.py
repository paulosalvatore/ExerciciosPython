"""
Exercício 11

Nome: Votação: Zona Eleitoral
Objetivo: Receber a idade da pessoa e, caso seja maior ou igual a 16 anos, pergunta a zona onde a pessoa mora e exibe a escola de votação.

1 - Escreva um programa que:
2 - Pergunte a idade da pessoa e, caso tenha menos do que 16 anos, informe que a pessoa não vota.
3 - Caso contrário, pergunte a zona onde a pessoa mora (zona oeste, leste, norte, sul ou centro) e exibe o local de votação de acordo com as regras a seguir:
4 - Pessoas que moram na zona oeste e zona norte votam na escola A.
5 - Pessoas que moram na zona leste votam na escola B.
6 - Pessoas que moram na zona sul ou no centro votam na escola C.
7 - Certifique-se de que seu código funciona mesmo que a pessoa digite: 'Oeste, OESTE ou oeste', por exemplo.
"""

# Resolução

idade = int(input("Qual a sua idade? "))

if (idade < 16):
	print("Você não pode votar.")
else:
	zona = input("Qual a zona onde você mora? (oeste, leste, norte, sul ou centro) ").lower()

	if (zona == "oeste" or zona == "norte"):
		print("Você vota na escola A.")
	elif (zona == "leste"):
		print("Você vota na escola B.")
	elif (zona == "sul" or zona == "centro"):
		print("Você vota na escola C.")
	else:
		print("Insira uma zona válida.")
