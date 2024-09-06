import math
n=int(input())


for _ in range(n):
    soldados = int(input())
    k= int((-1 + math.sqrt(1+8*soldados))//2)

    print(k)


# Calculando o número de fileiras (k) com base no número de guerreiros (n)
# Passo 1: Multiplicamos 8 pelo número de guerreiros
# Passo 2: Somamos 1 ao resultado anterior
# Passo 3: Calculamos a raiz quadrada dessa soma
# Passo 4: Subtraímos 1 do resultado da raiz
# Passo 5: Dividimos o resultado final por 2 para obter o valor de k

#k = (-1 + RAIZ(1 + 8 * n)) / 2
