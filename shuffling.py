def ins(b1, n):
    metade = n // 2
    b2 = [0] * n  # Vetor para o novo baralho
    i, j, pos = 0, metade, 0

    for k in range(metade):
        if j < n:
            b2[pos] = b1[j]
            j += 1
            pos += 1
        if i < metade:
            b2[pos] = b1[i]
            i += 1
            pos += 1
            
    # Se n for ímpar, adicionar a última carta da segunda metade
    if n % 2 != 0 and j < n:
        b2[pos] = b1[j]

    return b2


def main():
    qtd, tipo = input().split()
    qtd = int(qtd)


    original = list(range(1, qtd + 1))
    baralho = original.copy()

    contador = 0

    while True:
        if tipo == 'in':
            baralho = ins(baralho, qtd)
        else:
            baralho = out(baralho)
        
        contador += 1
        
        if baralho == original:
            break

    print(contador)

def out(baralho):
    metade = (len(baralho) + 1) // 2
    novo_baralho = []
    for i in range(metade):
        novo_baralho.append(baralho[i])
        if i + metade < len(baralho):
            novo_baralho.append(baralho[i + metade])
    return novo_baralho

main()
