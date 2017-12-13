"""
Exercício 14

Nome: Média Escolar
Objetivo: Escrever uma aplicação utilizando funções que calcule a média de um aluno.
Dificuldade: Intermediário

1 - Um professor, muito legal, fez 3 provas durante um semestre mas só vai levar em conta as duas notas mais altas para calcular a média.
2 - Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.
"""

# Resolução


# Função que solicita uma nota digitada pelo usuário e retorna o valor digitado no tipo 'float', que
# aceita números com casas decimais
def solicitar_nota():
	return float(input("Digite uma nota: "))


# Função que compara duas notas e retorna sempre a maior
def pegar_maior_nota(nota1, nota2):
	if nota1 > nota2:
		return nota1
	else:
		return nota2

# Função que compara duas notas e retorna sempre a menor
def pegar_menor_nota(nota1, nota2):
	if nota1 < nota2:
		return nota1
	else:
		return nota2


# Solicitamos as três notas
nota1 = solicitar_nota()
nota2 = solicitar_nota()
nota3 = solicitar_nota()

# Pegamos a maior nota entre a nota1 e a nota2
maior1 = pegar_maior_nota(nota1, nota2)

# Pegamos a maior nota entre a nota2 e a nota3
maior2 = pegar_maior_nota(nota2, nota3)

# Caso a maior nota (1) seja igual a maior nota (2), pegamos a maior nota entre a 1 e a 3
if maior1 == maior2:
	maior2 = pegar_maior_nota(nota1, nota3)

# Pegamos a maior nota entre as três notas
maior_nota = pegar_maior_nota(nota1, nota2)
maior_nota = pegar_maior_nota(maior_nota, nota3)

# Pegamos a menor nota entre as três notas
menor_nota = pegar_menor_nota(nota1, nota2)
menor_nota = pegar_menor_nota(menor_nota, nota3)

# Determinamos a media entre todas as notas
media_geral = (nota1 + nota2 + nota3) / 3

# Determinamos a media entre as duas maiores notas
media_maiores_notas = (maior1 + maior2) / 2

# Exibimos todas as variáveis na tela

print("Maior nota: {:.2f}.".format(maior_nota))
print("Menor nota: {:.2f}.".format(menor_nota))

print("Média entre todas as notas: {:.2f}.".format(media_geral))

print("Média entre as duas maiores notas: {:.2f}.".format(media_maiores_notas))

