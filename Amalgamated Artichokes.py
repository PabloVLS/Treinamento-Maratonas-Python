import math
numero=list(map(int , input().split()))
n=numero[5]
p=numero[0]
a=numero[1]
b=numero[2]
c=numero[3]
d=numero[4]
precos=[]


for i in range(n):
    preco = p * (math.sin( math.radians(a * i + b)) + math.cos(math.radians(c * i + d)) +2)
    #preco = p * (math.sin(a * i + b) + math.cos(c * i + d) + 2)
    precos.append(preco)

precoMinimo=precos[0]
maiorQueda=0

for preco in precos[1:]:
    queda = precoMinimo-preco

    maiorQueda = max(maiorQueda, queda)

    # Atualiza o preço mínimo encontrado até o momento
    precoMinimo = min(precoMinimo, preco)

if maiorQueda < 1e-6:
    print("0.00")
else:
    print(f"{maiorQueda:.9f}".rstrip('0').rstrip('.'))