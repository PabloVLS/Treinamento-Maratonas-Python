qtd=int(input())
result = 0.0

for i in range(qtd):
    num1,num2=map(float, input().split())
    mult=num1*num2
    result += mult


print(f"{result:.3f}")