import  sys
from msvcrt import kbhit

n=int(input())


for _ in range(n):
    linha = 0
    soldados = int(input())
    k=1
    while soldados >= k:
        soldados-=k
        k+=1
        linha+=1

    print(linha)