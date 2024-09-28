while True:
    a, b, c, x, y = map(int, input().split())
    if a + b + c + x + y == 0:
        break

    cartas = sorted([a, b, c], reverse=True)
    maior = cartas[0]
    segundaMaior = cartas[1]
    menor = cartas[2]

    cartasPrincipe = sorted([x, y], reverse=True)
    maiorPrincipe = cartasPrincipe[0]
    segundaPrincipe = cartasPrincipe[1]

    cartaUsada = set([a, b, c, x, y])

    if maiorPrincipe > maior:
        if segundaPrincipe > maior:
            for carta in range(1, 53):
                if carta not in cartaUsada:
                    print(carta)
                    break
            else:
                print("-1")
        elif segundaPrincipe > segundaMaior:
            for carta in range(1, 53):
                if carta not in cartaUsada and carta > segundaMaior:
                    print(carta)
                    break
            else:
                print("-1")
        else:
            for carta in range(1, 53):
                if carta not in cartaUsada and carta > maior:
                    print(carta)
                    break
            else:
                print("-1")

    else:
        if segundaPrincipe > segundaMaior:
            for carta in range(1, 53):
                if carta not in cartaUsada and carta > segundaMaior:
                    print(carta)
                    break
            else:
                print("-1")
        else:
            print("-1")
