import math
t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    result = (math.floor(n/3))*(math.floor(m/3))
    print(result)