qtd = int(input())

#Multiplique n por 567, depois divida o resultado por 9, adicione 7492, multiplique por 235,
#divida por 47 e, finalmente, subtraia 498.
for i in range(qtd):
    numero = int(input())
    numero = (((((numero*567)/9)+7492)*235)/47)-498
    numero = ((abs(numero)/10)%10)
    print(int(numero))