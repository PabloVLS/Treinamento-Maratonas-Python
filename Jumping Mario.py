
qtd = int(input())
for cont in range(1,qtd+1):
    qtdmuros = int(input())
    numeros = list(map(int , input().split()))

    baixo = 0
    alto = 0
    for i in range(1,len(numeros)):
        if numeros[i]>numeros[i-1]:
            alto+=1
        elif numeros[i]<numeros[i-1]:
            baixo+=1

    print(f"Case {cont}: {alto} {baixo}")