n=int(input())
for j in range(n):
    numeros = list(map(int , input().split()))
    casos=numeros[0]
    gnomos = numeros[1:]
    for i in range(casos - 1):
        if gnomos[i] != gnomos[i + 1] - 1:
            print(i + 2)  # Posição do rei (1-base)
            break
    

