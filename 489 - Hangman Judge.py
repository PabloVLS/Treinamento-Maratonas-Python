while True:
    erros = 0
    rodada = int(input()) 
    if rodada == -1:  
        break

    palavraCerta = input()  
    palavraTentada = input()  

    letraRestante = list(palavraCerta)

    for letra in palavraTentada:
        if letra in letraRestante:
             letraRestante = [l for l in letraRestante if l != letra]
            
        else:
            erros += 1 
            
        if not letraRestante:
            break
    
    print("Round", rodada)

    if erros >= 7:
        print("You lose.")
    elif not letraRestante:
        print("You win.")
    else:
        print("You chickened out.")
