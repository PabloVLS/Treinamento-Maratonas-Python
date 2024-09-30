qtd ,domi = input().split()
qtd = int(qtd)
total=0
valores = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    'T': 10,
    '9': 0,
    '8': 0,
    '7': 0
}

for i in range(qtd*4):
    carta=input()
    valor=carta[:-1]
    naipe=carta[-1]
    
    if naipe == domi:
        if valor=='J':
            total += 20
        elif valor=='9':
            total += 14
        else:
            total += valores.get(valor, 0)
    else:
        total += valores.get(valor, 0)
        
print(total)