"""
Exercício 23

Nome: Pedra, Papel e Tesoura
Objetivo: Criar um jogo de pedra, papel e tesoura, jogador versus computador.
Dificuldade: Intermediário

1 - Crie um programa que receba uma jogada do usuário (pedra, papel ou tesoura).
Exiba a mensagem: "Você jogou {}.", onde '{}' é a jogada do usuário.
2 - Faça com que seu jogo rode infinitamente, a menos que o usuário digite "sair".
3 - Caso o usuário digite "pedra, papel ou tesoura", prossiga com o jogo, caso ele digite "sair", encerre o jogo e caso ele digite qualquer outra coisa, pergunte a jogada novamente.
4 - Faça com que o programa ignore se o usuário digitou Pedra, PEDRA, ou pEdRa, ambos devem ser entendidos como "pedra".
5 - Gere uma jogada aleatória para o computador.
Exiba a mensagem: "Computador jogou {}.", onde '{}' é a jogada do computador.
6 - Exiba o resultado da jogada.
Pedra quebra Tesoura.
Tesoura corta Papel.
Papel embrulha Pedra.
7 - Caso o jogador tenha ganhado, exiba: "Você ganhou.", caso contrário, exiba: "Você perdeu.".
8 - Você também deverá criar um placar para o jogo, onde cada jogada que o jogador vencer, adicione 1 ponto ao placar do jogador e cada jogada que o computador vencer, adicione um ponto ao placar do computador.
Ao término da execução do programa (quando o jogador digitar "sair"), exiba a quantidade de rodas, a quantidade de pontos de cada um, se o jogador venceu, perdeu ou se deu empate.
"""

# Resolução

from random import randint

rodadas = 0
pontos_jogador = 0
pontos_computador = 0
empates = 0

while True:
	rodadas += 1

	print("Rodada {}".format(rodadas))

	jogada_usuario = input("Digite a sua jogada (Pedra, Papel ou Tesoura) ou 'sair' para sair do jogo: ").lower()

	if (jogada_usuario == "pedra" or
				jogada_usuario == "papel" or
				jogada_usuario == "tesoura"):

		print("Você jogou {}.".format(jogada_usuario))

		jogada_computador = randint(0, 3)

		if jogada_computador == 0:
			jogada_computador = "pedra"
		elif jogada_computador == 1:
			jogada_computador = "papel"
		else:
			jogada_computador = "tesoura"

		print("Computador jogou {}.".format(jogada_computador))

		vitoria = False
		empate = False

		if jogada_usuario == "pedra":
			if jogada_computador == "tesoura":
				print("Pedra quebra Tesoura.")
				vitoria = True
			elif jogada_computador == "papel":
				print("Papel embrulha Pedra.")
			else:
				print("Nada acontece.")
				empate = True
		elif jogada_usuario == "papel":
			if jogada_computador == "pedra":
				print("Papel embrulha Pedra.")
				vitoria = True
			elif jogada_computador == "tesoura":
				print("Pedra quebra Tesoura.")
			else:
				print("Nada acontece.")
				empate = True
		elif jogada_usuario == "tesoura":
			if jogada_computador == "papel":
				print("Tesoura corta Papel.")
				vitoria = True
			elif jogada_computador == "pedra":
				print("Pedra quebra Tesoura.")
			else:
				print("Nada acontece.")
				empate = True

		if empate:
			print("Rodada terminou em empate.")
			empates += 1
		elif vitoria:
			print("Você venceu a rodada.")
			pontos_jogador += 1
		else:
			print("Você perdeu a rodada.")
			pontos_computador += 1

		print("Rodada {} finalizada.".format(rodadas))
	elif jogada_usuario == "sair":
		break
	else:
		print("Insira uma jogada válida.")
		rodadas -= 1
	print()

print("Placa do Jogo:")
print("Pontos do Jogador: {}".format(pontos_jogador))
print("Pontos do Computador: {}".format(pontos_computador))
print("Empates: {}".format(empates))

if pontos_jogador > pontos_computador:
	print("Você venceu.")
elif pontos_computador > pontos_jogador:
	print("Você perdeu.")
else:
	print("O jogo terminou em empate.")
