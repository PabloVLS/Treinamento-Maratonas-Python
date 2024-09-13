qtd=int(input())

for i in range(qtd):
    entrada=input().strip()

    if entrada =="P=NP":
        print("skipped")
    else:
        if '+' in entrada:
            parte = entrada.split('+')
            a = int(parte[0])
            b = int(parte[1])
            result=a+b
            print(result)