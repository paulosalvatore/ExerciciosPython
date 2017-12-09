"""
Exercício 6

Nome: Catapulta
Objetivo: Receber o número de baterias e duração da bateria e calcular a quantidade de pedras que a catapulta irá soltar.
Dificuldade: Principiante

1 - Uma catapulta lançou 300 pedras em 5 baterias de 15 minutos, cada.
2 - Quantas pedras ela lançaria em 8 baterias de 7 minutos, cada?
3 - Crie um programa que receba os valores base para que a aplicação funcione de forma que, se alterarmos o número de bateriais e a duração de cada bateria, o programa funcione sem precisar de mais modificações.
"""

# Resolução

pedras_minuto = 300 / (5 * 15)
baterias = int(input("Informe quantas baterias: "))
duracao_bateria = int(input("Informe a duração de cada bateria: "))

pedras = pedras_minuto * baterias * duracao_bateria

print("A catapulta lançou {:.0f} pedras em {} baterias de {} minutos, cada.".format(pedras, baterias, duracao_bateria))
