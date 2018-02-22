"""
Exercício 29

Nome: POO - Políticos
Objetivo: Desenvolver uma aplicação orientada a objetos para controle de políticos.
Dificuldade: Avançado

1 - Criar as classes/atributos abaixo:

Políticos:
- Nome (texto)
- Nome Alternativo (texto)
- CPF (texto)
- Data de Nascimento (datetime)
- E-mail (texto)
- Gênero (apenas uma letra, F/M)
- Lista de Partidos Políticos (Lista de Classe)
- Partido atual (Classe)
- Lista de Candidaturas (Lista de Classe)

Partidos Políticos:
- Nome
- Sigla
- Número_TSE
- Lista de Políticos

Candidaturas:
- Status da Candidatura (Classe)
- Cidade (texto)
- Eleito (bool)
- Político (Classe)
- Partido (Classe)
- Data da Última Atualização (datetime)

Status da Candidatura:
- Nome (texto)

2 - Criar os seguintes métodos:
Políticos:
- validar_cpf(): Irá receber uma informação e retornar se é um CPF válido ou não.
- calcular_idade(): Irá pegar a data de nascimento do político e retornar sua idade.
- validar_email(): Irá pegar uma informação e retornar se é um e-mail válido ou não.
- pegar_genero(): Irá pegar o gênero e retornar o gênero completo (Ex.: M irá retornar Masculino).
- adicionar_partido(): Adiciona um partido ao político
Ao adicionar um partido a um político, define esse como o partido atual do político.
Além disso, quando adicionar um partido a um político, referenciar esse político na lista de políticos do partido em questão.
- abandonar_partido(): Checa se tem um partido atual, se tiver, remove o partido atual. Também remove o político da lista de políticos do partido.
- adicionar_candidatura(): Adiciona uma nova candidatura ao político.

Partidos Políticos:
- adicionar_politico(): Adiciona um político na lista de políticos da classe. Checa se esse político já está na lista, caso esteja, exibe a mensagem a não adiciona.
- remover_politico(): Remove o político da lista de políticos.

Candidaturas:
- atualizar(): Atualiza a candidatura, atualizando o atributo eleito.
Sempre que uma candidatura for criada ou atualizada, o atributo 'ultima_atualizacao' deve ser atualizado.
"""

from datetime import datetime


class Politicos:
	nome = None
	nome_alternativo = None
	cpf = None
	data_nascimento = None
	idade = None
	email = None
	genero = None
	partidos_politicos = None
	partido_atual = None
	candidaturas = None

	def __init__(self, nome, cpf, data_nascimento, email, genero, nome_alternativo=None):
		self.nome = nome
		self.nome_alternativo = nome_alternativo
		# Validar o CPF
		# Se tiver OK, cria o objeto normalmente
		# Caso contrário, não cria o objeto
		self.cpf = self.validar_cpf(cpf)
		# Data de Nascimento Formato: 27/11/1993 - Preciso transformar
		# em objeto datetime
		self.data_nascimento = self.transformar_data(data_nascimento)
		self.calcular_idade()
		self.email = self.validar_email(email)
		self.genero = self.pegar_genero(genero)
		self.partidos_politicos = []
		self.partido_atual = None
		self.candidaturas = []

	def pegar_digito(self, numeros, fator):
		total = 0

		for numero in numeros:
			resultado = fator * int(numero)
			total = total + resultado
			fator = fator - 1

		divisao, resto = divmod(total, 11)

		if resto < 2:
			digito = 0
		else:
			digito = 11 - resto

		return str(digito)

	def validar_cpf(self, cpf):
		if cpf.count("-") == 1 and cpf.count(".") == 2 and len(cpf) == 14:
			cpf_separado = cpf.split("-")
			numeros = cpf_separado[0].replace(".", "")
			digitos = cpf_separado[1]
			digito1 = self.pegar_digito(numeros, 10)
			digito2 = self.pegar_digito(numeros + digito1, 11)

			if digito1 == digitos[0] and digito2 == digitos[1]:
				return cpf

		print("CPF do Político {} inválido.".format(self.nome))

	def calcular_idade(self):
		agora = datetime.now()
		diferenca = agora - self.data_nascimento
		self.idade = diferenca.days // 365

	def transformar_data(self, data):
		data = data.split("/")
		dia = int(data[0])
		mes = int(data[1])
		ano = int(data[2])
		data = datetime(ano, mes, dia)
		return data

	def validar_email(self, email):
		if email.count("@") == 1:
			email_separado = email.split("@")
			if email_separado[1].count(".") >= 1:
				return email

		print("E-mail do Político {} inválido.".format(self.nome))

	def pegar_genero(self, genero):
		genero = genero.upper()

		if genero == "F":
			return "Feminino"
		elif genero == "M":
			return "Masculino"
		else:
			return "Genero não informado"

	def adicionar_partido(self, partido):
		if self.partido_atual == partido:
			print("Político {} já está no partido {}.".format(self.nome, partido.nome))
		else:
			self.partidos_politicos.append(partido)
			print("Político {} foi adicionado ao partido {}.".format(self.nome, partido.nome))
			partido.adicionar_politico(self)
			self.partido_atual = partido

	def abandonar_partido(self):
		self.partido_atual.remover_politico(self)
		print("Político {} foi removido do partido {}.".format(self.nome, self.partido_atual.nome))
		self.partido_atual = None

	def adicionar_candidatura(self, status, cidade, partido, eleito=None):
		candidatura = Candidaturas(status, cidade, partido, self, eleito)
		self.candidaturas.append(candidatura)
		print("A candidatura {} foi adicionada ao político {}.".format(candidatura.status.nome, self.nome))


class Partidos:
	nome = None
	sigla = None
	numero_tse = None
	politicos = None

	def __init__(self, nome, sigla, numero_tse):
		self.nome = nome
		self.sigla = sigla
		self.numero_tse = numero_tse
		self.politicos = []

	def adicionar_politico(self, politico):
		if self.politicos.count(politico) > 0:
			print("Político {} já está no partido {}.".format(politico.nome, self.nome))
		else:
			self.politicos.append(politico)

	def remover_politico(self, politico):
		if self.politicos.count(politico) == 1:
			self.politicos.remove(politico)


class Candidaturas:
	status = None
	cidade = None
	eleito = None
	politico = None
	partido = None
	ultima_atualizacao = None

	def __init__(self, status, cidade, partido, politico, eleito=None):
		self.status = status
		self.cidade = cidade
		self.eleito = eleito
		self.partido = partido
		self.politico = politico
		self.atualizar_ultima_atualizacao()

	def atualizar(self, eleito):
		self.eleito = eleito
		print("Atributo eleito da candidatura {} foi atualizado para {}.".format(self.status.nome, eleito))
		self.atualizar_ultima_atualizacao()

	def atualizar_ultima_atualizacao(self):
		self.ultima_atualizacao = datetime.now()


class StatusCandidaturas:
	nome = None

	def __init__(self, nome):
		self.nome = nome


# Chamar classes/objetos/métodos

# Políticos
joao = Politicos("João", "430.910.048-13", "27/11/1993", "joao@gmail.com", "M")
maria = Politicos("Maria", "123.456.789-20", "10/11/1975", "maria@gmail.com", "F", "Maria do Carmo")

# Partidos
dem = Partidos("Partido dos Democratas", "DEM", 80)
pv = Partidos("Partido Verde", "PV", 44)

# Status
deferido = StatusCandidaturas("Deferido")
renuncia = StatusCandidaturas("Renúncia")
impugnado = StatusCandidaturas("Impugnado")
indeferido = StatusCandidaturas("Indeferido")

joao.adicionar_partido(dem)

maria.adicionar_partido(pv)

joao.abandonar_partido()

joao.adicionar_partido(pv)

joao.adicionar_candidatura(deferido, "São Paulo", pv)

joao.candidaturas[0].atualizar(eleito=True)

print(joao.nome, joao.idade, joao.cpf, joao.email)
