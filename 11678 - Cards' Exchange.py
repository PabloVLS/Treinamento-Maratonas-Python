while True:
    a, b = map(int, input().split())
    if a+b ==0:
        break
    
    
    alice = list(map(int , input().split()))
    betty = list(map(int , input().split()))
    
    
    cartaNaoRepA = list(set(alice))
    cartaNaoRepB = list(set(betty))
    
    repetidas = len(set(cartaNaoRepA) & set(cartaNaoRepB)) 
    
    trocas = min(len(cartaNaoRepA), len(cartaNaoRepB)) - repetidas
    print(trocas)
    
 
    
 # for alice in range(a):
#     cartaAlice = list(map(int , input().split()))
# 
# for betty in range(b):
#     cartaBetty = list(map(int,input().split()))
# 
# for cont in range(a-1):
#     if cartaAlice[cont]!=cartaAlice[cont+1]:
#         cartaNaoRepA.append(cartaAlice[cont])
# cartaNaoRepA.append(cartaAlice[-1])
#         
# for cont in range(b-1):
#     if cartaBetty[cont]!=cartaBetty[cont+1]:
#         cartaNaoRepB.append(cartaBetty[cont])
# cartaNaoRepB.append(cartaBetty[-1])
# 
# if a>=b:
#     for cont1 in range(len(cartaNaoRepA)):
#         repetida=0
#         for cont2 in range(len(cartaNaoRepA)):
#             if cartaNaoRepA[cont1] == cartaNaoRepB[cont2]:
#                 repetida =1
#                 break
#         contRep+=repetida
#         
#     trocas = len(cartaNaoRepB)-repetida
# else:
#     for cont1 in range(len(cartaNaoRepB)):
#         repetida=0
#         for cont2 in range(len(cartaNaoRepA)):
#             if cartaNaoRepB[cont1] == cartaNaoRepA[cont2]:
#                 repetida =1
#                 break
#         contRep+=repetida
#         
#     trocas = len(cartaNaoRepA)-contRep
#     
# print(trocas)
