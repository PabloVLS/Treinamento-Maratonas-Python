qtd = int(input())

for i in range(qtd):
    n = int(input())
    valores = []

    for i in range(n):
        valores.append(int(input()))

    diferenca = float('-inf')
    maiorVeterano = valores[0]

    for j in range(1,n):
        diferenca = max(diferenca, maiorVeterano - valores[j]) #diferença ta recebendo maiorVeterano - valores[j]
        maiorVeterano = max(maiorVeterano, valores[j])

    print(diferenca)