"""
Exercício 15

Nome: Gastos da Viagem
Objetivo: Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem, aluguel de carro e gastos extras de uma viagem para uma determinada cidade.
Dificuldade: Intermediário

Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

Passagem
2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.

Aluguel de Carro
3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.

Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!

Gastos Extras
5 - Modifique essa nova função criada e adicione um terceiro argumento: 'gastos_extras' e some esse valor ao total da viagem.
Exiba no console o custo total de uma viagem de 12 dias para 'Manaus' gastando R$ 800,00 adicionais.
"""

# Resolução

# Definimos a função que recebe um determinado número de noites e retorna o custo do hotel, onde cada noite equivale a R$ 140,00.
def custo_hotel(noites):
	return noites * 140


# Definimos a função que recebe um determinado nome de cidade e retorna o custo da passagem de avião para essa cidade.
def custo_aviao(cidade):
	custo = 0

	if cidade == "São Paulo":
		custo = 312.0
	elif cidade == "Porto Alegre":
		custo = 447.0
	elif cidade == "Recife":
		custo = 831.0
	elif cidade == "Manaus":
		custo = 986.0

	return custo


# Definimos a função que recebe um determinado número de dias e retorna o custo do aluguel de carro, onde cada dia equivale a R$ 40,00, aplicando um determinado desconto dependendo do número de dias que a pessoa utilizar o serviço.
def custo_carro(dias):
	custo = dias * 40

	if dias >= 7:
		custo -= 50
	elif dias >= 3:
		custo = custo - 20

	return custo


# Definimos a função que recebe todos os valores: 'noites, cidade, dias com o carro e o gasto extra' e retorna o custo total da viagem, calculando os valores com as respectivas funções declaradas anteriormente.
def custo_total(noites, cidade, dias_carro, gasto_extra):
	return custo_hotel(noites) + custo_aviao(cidade) + custo_carro(dias_carro) + gasto_extra


# Pegamos as informações digitadas pelo usuário.
noites = int(input("Quantas noitas você irá passar? "))
cidade = input("Para qual cidade você vai? ")
dias_carro = int(input("Quantos dias você usará o carro? "))
gasto_extra = float(input("Qual será o seu gasto extra?"))

# Passamos os valores digitados para a função que irá calcular o custo total da viagem.
custo = custo_total(noites, cidade, dias_carro, gasto_extra)

# Exibimos na tela o custo total da viagem, detalhando algumas informações digitadas anteriormente.
print("O custo total para ir para {}, ficar {} noites, usar o carro por {} dias e gastar R$ {:.2f} a mais é de R$ {:.2f}".format(cidade, noites, dias_carro, gasto_extra, custo))
