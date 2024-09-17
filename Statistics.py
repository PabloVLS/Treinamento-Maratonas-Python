import  sys
menor = 100000000
maior = -100000000
cont = 0
for linha in sys.stdin:
    cont+=1
    numeros = list(map(int,linha.split()))
    qtd = numeros[1:]#esse : ta dizendo que do 1 pra frente e criada outra lista
    for valor in qtd: # e daqui o valor vai ate o final da lista
        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

    print(f"Case {cont}: {menor} {maior} {maior - menor}")

    menor = 99999
    maior = 0
