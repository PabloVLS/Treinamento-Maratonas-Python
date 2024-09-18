import sys
import re

while True:
    try:
        nome1 = input().strip()
        nome2 = input().strip()
       
        
        letras1 = re.sub(r'[^a-zA-Z]','',nome1)
        total1=0
        for letra1 in letras1:
            valor1 = ord(letra1.upper())- ord('A')+1
            total1+=valor1
        total1=total1%9
        if total1 ==0:
            total1 =9
        
        letras2 = re.sub(r'[^a-zA-Z]','',nome2)
        total2=0
        for letra2 in letras2:
            valor2 = ord(letra2.upper())- ord('A')+1
            total2+=valor2
        total2=total2%9
        if total2 == 0:
            total2 =9
        
        if total1>total2:
            caso = (total2/total1)*100
        else:
            caso = (total1/total2)*100
            
        print(f"{caso:.2f} %")
    except EOFError:
        break