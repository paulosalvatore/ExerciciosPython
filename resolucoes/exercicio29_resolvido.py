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
