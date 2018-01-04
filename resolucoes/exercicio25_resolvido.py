"""
Exercício 25

Nome: Cadastro de Pessoas
Objetivo: Criar uma aplicação que cadastre, liste, consulte e remova pessoas utilizando um dicionário.
Dificuldade: Avançado

1 - Crie uma aplicação que rode infinitamente.
2 - A aplicação deverá perguntar ao usuário se deseja realizar uma das seguintes ações (independente se digitar maiúsculo ou minúsculo):
'C' ou 'Cadastrar' irá cadastrar uma nova pessoa ao dicionário;
'L' ou 'Listar' irá listar as pessoas cadastradas no dicionário;
'R' ou 'Remover' irá remover uma pessoa (buscando pelo nome);
'E' ou 'Editar' irá editar uma pessoa previamente cadastrada;
3 - A pessoa terá os seguintes dados: nome, sobrenome, telefone e CPF.
4 - A cada ação realizada, o sistema deverá informar uma mensagem de sucesso.
5 - Em caso de ações que procurem pessoas já cadastradas no sistema (editar ou remover), caso a pessoa não seja encontrada, exiba essa mensagem para o usuário.
6 - Você deverá declarar uma função que recebe um nome de pessoa digitado pelo usuário e procure no dicionário por aquela pessoa. Caso encontre, retorne a pessoa encontrada. Caso contrário, exiba uma mensagem de que a pessoa não foi encontrada e pergunte novamente pelo nome da pessoa.
7 - A qualquer momento da aplicação, o usuário poderá cadastrar, listar, remover ou editar pessoas.
8 - Caso ele acesse alguma das opções acima e não queira prosseguir, digitar a palavra 'cancelar' irá retornar ao menu principal.
"""

# Resolução

# Lista com todas as pessoas do sistema
# As pessoas serão cadastradas com a aplicação sendo executada.
pessoas = []

# Funções


def pegar_informacao_digitada(mensagem, obrigatoria=True):
	informacao = ""

	while informacao == "":
		informacao = input(mensagem)

		if not obrigatoria:
			break

	return informacao


def localizar_pessoa(campo, exibicao_campo):
	informacao = pegar_informacao_digitada("{}: ".format(exibicao_campo)).lower()

	if informacao == "cancelar":
		return False

	for pessoa in pessoas:
		if pessoa[campo].lower() == informacao.lower():
			return pessoa

	print("Pessoa não encontrada. Tente novamente.")
	return False


def nova_pessoa(pessoa=False):
	if not pessoa:
		obrigatoria = True
		pessoa = {}
	else:
		obrigatoria = False

	nome = pegar_informacao_digitada("Nome: ", obrigatoria)
	sobrenome = pegar_informacao_digitada("Sobrenome: ", obrigatoria)
	telefone = pegar_informacao_digitada("Telefone: ", obrigatoria)
	cpf = pegar_informacao_digitada("CPF: ", obrigatoria)
	email = pegar_informacao_digitada("E-mail: ", obrigatoria)

	if nome != "":
		pessoa["nome"] = nome

	if sobrenome != "":
		pessoa["sobrenome"] = sobrenome

	if telefone != "":
		pessoa["telefone"] = telefone

	if cpf != "":
		pessoa["cpf"] = cpf

	if email != "":
		pessoa["email"] = email

	return pessoa


def cadastrar_pessoa():
	print("Para cadastrar uma pessoa, digite os dados completos.")

	pessoa = nova_pessoa()

	acao = input("Pressione a tecla 'enter' para realizar o cadastro ou digite 'cancelar' para cancelar o cadastro... ").lower()

	if acao == "cancelar":
		print("Cadastro cancelado.")
	else:
		pessoas.append(pessoa)

		print("Pessoa cadastrada com sucesso.".format(pessoa["nome"]))


def listar_pessoas():
	if len(pessoas) == 0:
		print("No momento não há pessoas cadastradas no sistema.")
	else:
		print("Lista de pessoas cadastradas:")
		for pessoa in pessoas:
			print("\tNome: {} {} - Telefone: {} - CPF: {}".format(pessoa["nome"], pessoa["sobrenome"], pessoa["telefone"], pessoa["cpf"]))


def remover_pessoa():
	print("Para remover uma pessoa, informe o nome dela para localizar o cadastro ou digite 'cancelar' para cancelar a ação.")
	pessoa = localizar_pessoa("nome", "Nome")

	if not pessoa:
		print("Ação cancelada.")
	else:
		pessoas.remove(pessoa)
		print("Pessoa removida com sucesso.")


def editar_pessoa():
	print("Para editar uma pessoa, informe o nome dela para localizar o cadastro ou digite 'cancelar' para cancelar a ação.")
	pessoa = localizar_pessoa("nome", "Nome")

	if not pessoa:
		print("Ação cancelada.")
	else:
		print("Pessoa localizada, digite os novos dados abaixo:")
		indice_pessoa = pessoas.index(pessoa)
		pessoas[indice_pessoa] = nova_pessoa(pessoa)
		print("Pessoa editada com sucesso.")

# Execução Principal do Programa

print("Cadastro de Pessoas")
print("Nessa aplicação você poderá cadastrar, listar, remover ou editar pessoas.")

while True:
	print("Digite 'C' ou 'Cadastrar' para Cadastrar Pessoas.")
	print("Digite 'L' ou 'Listar' para Listar Pessoas.")
	print("Digite 'R' ou 'Remover' para Remover Pessoas.")
	print("Digite 'E' ou 'Editar' para Editar Pessoas.")
	print("Caso queira cancelar alguma ação, digite 'Cancelar'.")
	acao = input("Escolha uma das ações para prosseguir: ").lower()

	if acao == "c" or acao == "cadastrar":
		cadastrar_pessoa()
	elif acao == "l" or acao == "listar":
		listar_pessoas()
	elif acao == "r" or acao == "remover":
		remover_pessoa()
	elif acao == "e" or acao == "editar":
		editar_pessoa()
	else:
		print("Insira uma opção válida.")

	input("Digite qualquer coisa para prosseguir... ")
	print("------------------------------------------")
