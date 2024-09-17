while True:
    dados = list(map(int, input().split()))
    if sum(dados) == 0:
        break

    #do jgoador 1
    if dados[0] < dados[1]:
        dados[0], dados[1] = dados[1], dados[0]

    if (dados[0] == 2 and dados[1] == 1) or (dados[0] == 1 and dados[1] == 2):
        jogador1 = (3, 0)
    elif dados[0] == dados[1]:
        jogador1 = (2, dados[0])
    else:
        jogador1 = (1, dados[0] * 10 + dados[1])

    #do jogador 2
    if dados[2] < dados[3]:
        dados[2], dados[3] = dados[3], dados[2]

    if (dados[2] == 2 and dados[3] == 1) or (dados[2] == 1 and dados[3] == 2):
        jogador2 = (3, 0)
    elif dados[2] == dados[3]:
        jogador2 = (2, dados[2])
    else:
        jogador2 = (1, dados[2] * 10 + dados[3])


    if jogador1 > jogador2:
        print("Player 1 wins.")
    elif jogador1 < jogador2:
        print("Player 2 wins.")
    else:
        print("Tie.")
