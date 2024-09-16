qtd = int(input())

for i in range(1, qtd + 1):
    numeros = list(map(int, input().split()))
    corredores = numeros[1:]
    
    maior = 0
    for rapido in corredores:
        if rapido >= maior:
            maior = rapido
    
    print(f"Case {i}: {maior}")
