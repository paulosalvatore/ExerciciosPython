"""
Exercício 13

Nome: Convertendo Celsius/Farenheit
Objetivo: Escrever duas funções de conversão, uma de graus celsius em farenheit e a outra que faça o contrário.
Dificuldade: Principiante

1 - Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
2 - Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão escolhida é realizada.
3 - Se C é a temperatura em Celsius e F em farenheit, as fórmulas de conversão são:
C = 5 * (F - 32) / 9
F = (9 * C / 5) + 32
"""

"""
Exercício 13

Nome: Convertendo Celsius/Farenheit
Objetivo: Escrever duas funções de conversão, uma de graus celsius em farenheit e a outra que faça o contrário.

1 - Crie um aplicativo de conversão entre as temperaturas Celsius e Farenheit.
2 - Primeiro o usuário deve escolher se vai entrar com a temperatura em Célsius ou Farenheit, depois a conversão escolhida é realizada.
3 - Se 'c' é a temperatura em Celsius e 'f' em farenheit, as fórmulas de conversão são:
c = 5 * (f - 32) / 9
f = (9 * c / 5) + 32
"""

# Resolução


def celsius():
	c = float(input("Digite a temperatura em graus Celsius: "))
	f = (9 * c / 5) + 32
	print("A temperatura {:.2f}ºC é equivalente a {:.2f}ºF.".format(c, f))


def farenheit():
	f = float(input("Digite a temperatura em graus Farenheit: "))
	c = 5 * (f - 32) / 9
	print("A temperatura {:.2f}ºF é equivalente a {:.2f}ºC.".format(f, c))

temperatura_escolhida = input("Escolha qual temperatura quer converter (C = Celsius e F = Farenheit): ").upper()

if temperatura_escolhida == "C":
	celsius()
elif temperatura_escolhida == "F":
	farenheit()
else:
	print("Escolha uma temperatura correta.")
