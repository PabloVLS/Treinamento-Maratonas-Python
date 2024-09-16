case_number = 1

while True:
    n = int(input())
    
    if n == 0:
        break
    
    events = list(map(int, input().split()))
    
    motivos = 0
    presentes = 0
    
    for event in events:
        if event > 0:
            motivos += 1
        elif event == 0:
            presentes += 1
    
    emoogle_balance = motivos - presentes
    
    print(f"Case {case_number}: {emoogle_balance}")
    
    case_number += 1
