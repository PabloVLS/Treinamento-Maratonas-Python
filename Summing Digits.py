soma = 0

def retirandoDigito(numero):
    somador=0
    while numero >0:
        digito = numero%10
        somador += digito
        numero = numero//10

    return somador

while True:
    n=int(input())
    if n==0:
        break
    while n>=10:
        n=retirandoDigito(n)


    print(n)