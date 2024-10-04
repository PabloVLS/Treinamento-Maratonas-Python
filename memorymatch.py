
qtd = int(input())
qtdjogadas = int(input())

cont = 0  
jogadas = []  


for i in range(qtdjogadas):
    roud = input().split()  
    jogadas.append((int(roud[0]), int(roud[1]), roud[2], roud[3])) 

cartas_encontradas = set() 


for i in range(qtdjogadas):
    carta1_pos, carta2_pos, carta1_nome, carta2_nome = jogadas[i]
    

    
    
    
    for k in range(i + 1, qtdjogadas):
        outra_carta1_pos, outra_carta2_pos, outra_carta1_nome, outra_carta2_nome = jogadas[k]
        

        if carta1_nome == outra_carta1_nome and carta1_pos != outra_carta1_pos:
            cartas_encontradas.add(carta1_pos)
            cartas_encontradas.add(outra_carta1_pos)
            cont += 1
            print(f"Entrou:{carta1_nome}{carta1_pos} ,{outra_carta1_nome} {outra_carta1_pos}")
            
            
        if carta1_nome == outra_carta2_nome and carta1_pos != outra_carta2_pos:
            cartas_encontradas.add(carta1_pos)
            cartas_encontradas.add(outra_carta2_pos)
            cont += 1
            print(f"Entrou:{carta1_nome}{carta1_pos} ,{outra_carta2_nome} {outra_carta2_pos}")
            

        if carta2_nome == outra_carta2_nome and carta2_pos != outra_carta2_pos:
            cartas_encontradas.add(carta2_pos)
            cartas_encontradas.add(outra_carta2_pos)
            cont += 1
            print(f"Entrou:{carta2_nome}{carta2_pos} ,{outra_carta2_nome} {outra_carta2_pos}")
            
            
        if carta2_nome == outra_carta1_nome and carta2_pos != outra_carta1_pos:
            cartas_encontradas.add(carta2_pos)
            cartas_encontradas.add(outra_carta1_pos)
            cont += 1
            print(f"Entrou:{carta2_nome}{carta2_pos} ,{outra_carta1_nome} {outra_carta1_pos}")
            

print(cont)
