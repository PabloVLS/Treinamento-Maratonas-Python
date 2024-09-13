t0, alpha = map(int, input().split())

# Caso especial: quando alpha é 1
if alpha == 1:
    if t0 == 0:
        print("ALL GOOD")  # As escalas são sempre iguais
    else:
        print("IMPOSSIBLE")  # Não existe uma temperatura em que as escalas sejam iguais
else:
    # Calcula a temperatura onde T1 = T2 usando a fórmula T1 = t0 / (1 - alpha)
    T1 = t0 / (1 - alpha)

    # Exibe a temperatura com precisão de 6 casas decimais
    print(f"{T1:.6f}")