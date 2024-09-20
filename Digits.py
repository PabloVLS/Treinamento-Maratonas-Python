import sys
for valor in sys.stdin:
    valor = valor.strip()
    if valor == "END":
        break
    i = 1

    while True:
        proximo_valor = str(len(valor))

        if proximo_valor == valor:
            print(i)
            break

        valor = proximo_valor
        i += 1
