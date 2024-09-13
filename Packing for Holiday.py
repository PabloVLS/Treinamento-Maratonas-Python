contador = 1
casos_teste = int(input())

for _ in range(casos_teste):
    comprimento, largura, altura = map(int, input().split())

    print(f"Case {contador}: ", end="")
    if comprimento <= 20 and largura <= 20 and altura <= 20:
        print("good")
    else:
        print("bad")
    contador += 1
