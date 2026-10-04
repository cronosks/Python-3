#========================================================
#              Game: Pedra, papel e tesoura
#========================================================

import random

print("===================================")
print("     PEDRA, PAPEL E TESOURA")
print("===================================")

print("Escolha sua jogada:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

jogador = int(input("\nDigite sua opção: "))

if jogador < 1 or jogador > 3:
    print("Opção inválida! Escolha entre 1 e 3.")

else:
    computador = random.randint(1, 3)

    if jogador == 1:
        escolha_jogador = "Pedra"
    elif jogador == 2:
        escolha_jogador = "Papel"
    else:
        escolha_jogador = "Tesoura"

    if computador == 1:
        escolha_computador = "Pedra"
    elif computador == 2:
        escolha_computador = "Papel"
    else:
        escolha_computador = "Tesoura"

    print("\n===================================")
    print("           RESULTADO")
    print("===================================")

    print("Você escolheu: {}" .format(escolha_jogador))
    print("Computador escolheu: {}" .format(escolha_computador))

    if jogador == computador:
        print("Resultado: EMPATE!")

    elif (jogador == 1 and computador == 3) or \
         (jogador == 2 and computador == 1) or \
         (jogador == 3 and computador == 2):
        print("Resultado: VOCÊ VENCEU! 🎉")

    else:
        print("Resultado: VOCÊ PERDEU!")

print("===================================")