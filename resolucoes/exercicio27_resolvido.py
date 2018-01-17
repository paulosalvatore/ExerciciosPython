"""
Exercício 27

Nome: Urna Eletrônica
Objetivo: Desenvolver um sistema de urna eletrônica que funcione apenas para a eleição de prefeito de uma cidade.
Dificuldade: Avançado

1 - Criar um dicionário com informações básicas dos candidatos à prefeitura.
2 - A aplicação deverá funcionar exatamente como uma urna eletrônica, contabilizando
votos válidos, brancos e nulos.
3 - Exiba para o usuário: "Informe seu voto para a prefeitura de São Paulo (2 dígitos): "
4 - A pessoa também pode digitar 'branco' em vez de um número.
5 - Assim que o usuário digitar um número, verifique se é um político existente e se
o político possui aquele cargo específico.
6 - Caso possua, informe o nome do político e o partido e peça para o usuário informar
uma ação: confirmar, corrigir ou cancelar.
- Confirmar computa o voto.
- Corrigir pergunta o voto novamente.
- Cancelar pergunta o voto novamente.
7 - Coloque um comando 'encerrar votação' que finaliza a votação e exibe as informações abaixo:
- Informar a quantidade de votos válidos, brancos e nulos;
- Checar se o político mais votado possui mais de 50% dos votos ou se haverá segundo turno.
- Caso tenha vencedor: Informar quem ganhou e qual a porcentagem de votos que ele teve;
- Exibir na tela um político por linha, com a quantidade de votos recebidos e a porcentagem equivalente.
"""

politicos = [
	{
		"nome": "José",
		"partido": "PT",
		"numero": 13,
		"votos": 0
	},
	{
		"nome": "Maria",
		"partido": "PV",
		"numero": 45,
		"votos": 0
	},
	{
		"nome": "Paulo",
		"partido": "PSDB",
		"numero": 43,
		"votos": 0
	},
	{
		"nome": "Roberta",
		"partido": "PMDB",
		"numero": 32,
		"votos": 0
	}
]

brancos = []
nulos = []


# Funções para processar a eleição


def pegar_voto():
	return input("Digite o número do politico que deseja votar ou 'branco' para votar em branco: ").lower()


def procurar_politico(voto):
	for politico in politicos:
		if str(politico["numero"]) == voto:
			return politico

	return None


def validar_voto(voto):
	politico = None

	if voto == "branco":
		print("Você votou em branco.")
	else:
		politico = procurar_politico(voto)

		if politico:
			print("O voto '{}' corresponde ao político '{}' do partido '{}'.".format(voto, politico["nome"], politico["partido"]))
		else:
			print("Nenhum político para o voto '{}' foi encontrado. Se prosseguir, seu voto será anulado.".format(voto))

	acao = input("Deseja confirmar, corrigir ou cancelar: ").lower()

	if acao == "confirmar":
		contabilizar_voto(voto, politico)
	elif acao == "corrigir":
		print("Você selecionou a opção de corração do voto. Informe-o novamente.")
	else:
		print("Você cancelou a informação do voto atual. Informe-o novamente.")


def contabilizar_voto(voto, politico):
	if voto == "branco":
		brancos.append(voto)
		print("O seu voto em branco foi contabilizado.")
	if politico:
		politico["votos"] += 1
		print("O seu voto para o político '{}' foi contabilizado.".format(politico["nome"]))
	else:
		nulos.append(voto)
		print("O seu voto foi anulado.")


# Funções para exibir o resultado da eleição


def pegar_total_votos_validos():
	votos_validos = 0

	for politico in politicos:
		votos_validos += politico["votos"]

	return votos_validos


def exibir_votos():
	print("Votos Válidos: {}.".format(pegar_total_votos_validos()))
	print("Votos Brancos: {}.".format(len(brancos)))
	print("Votos Nulos: {}.".format(len(nulos)))


def pegar_porcentagem_votos(politico):
	votos_validos = pegar_total_votos_validos()
	return politico["votos"] * 100 / votos_validos


def exibir_politico(politico):
	porcentagem = pegar_porcentagem_votos(politico)
	print("Político '{}' do partido '{}' recebeu '{}' voto{} e ficou com '{}%' dos votos válidos.".format(politico["nome"], politico["partido"], "" if politico["votos"] == 1 else "s", politico["votos"], porcentagem))


def exibir_vencedor():
	primeiro_lugar = None
	segundo_lugar = None
	for politico in politicos:
		if not primeiro_lugar or politico["votos"] > primeiro_lugar["votos"]:
			if primeiro_lugar:
				segundo_lugar = primeiro_lugar

			primeiro_lugar = politico
		elif not segundo_lugar or politico["votos"] > segundo_lugar["votos"]:
			segundo_lugar = politico

	porcentagem = pegar_porcentagem_votos(primeiro_lugar)
	if porcentagem >= 50:
		print("O vencedor da eleição é o político '{}' com '{}%' dos votos válidos.".format(primeiro_lugar["nome"], porcentagem))
	else:
		print("A votação encerrou em segundo turno.")
		print("Os políticos que vão para o segundo turno são:")
		exibir_politico(primeiro_lugar)
		exibir_politico(segundo_lugar)


def exibir_politicos():
	print("Resultado geral da votação")
	for politico in politicos:
		exibir_politico(politico)


while True:
	voto = pegar_voto()

	if voto == "encerrar_votacao":
		print("Votação encerrada com sucesso.")
		break

	validar_voto(voto)

exibir_votos()
exibir_vencedor()

print("__________________________________")

exibir_politicos()
