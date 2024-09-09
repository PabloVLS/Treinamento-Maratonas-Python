qtd = int(input())
meses = int(input())
dados = int()
for i in range(meses):
    gasto = int(input())
    dados += gasto

qtd = (qtd*meses)+qtd
print(qtd-dados)