while True:
    y1 = 0
    x1 = 0

    a,b,c,x,y = map(int, input().split())
    if a+b+c+x+y == 0:
        break
    cartas = sorted([a, b, c], reverse=True)
    maior = cartas[0]
    segundaMaior = cartas[1]

    if x > cartas[0]:
        x1 += 1
    if x > cartas[1]:
        x1 += 1
    if x > cartas[2]:
        x1 += 1

    if y > cartas[0]:
        y1 += 1
    if y > cartas[1]:
        y1 += 1
    if y > cartas[2]:
        y1 += 1


    if y1 ==0 or x1 ==0:
        print("-1")
    else:
        cartaUsada= set([a,b,c,x,y])
        for carta in range(1,53):
            if carta not in cartaUsada:
                if carta>cartas[1]:
                    print(carta)
                    break
        else:
            print("-1")