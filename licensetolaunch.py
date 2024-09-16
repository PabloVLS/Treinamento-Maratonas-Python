n=int(input())
valor=100001
j=-1
detrito = list(map(int , input().split()))
for i in range(n):
    if valor > detrito[i]:
        valor = detrito[i]
        j=i
print(j)

