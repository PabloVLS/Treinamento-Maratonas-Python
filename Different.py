import sys
for linha in sys.stdin:
    num1,num2 = map(int, linha.split())
    result=abs(num1-num2)
    print(result)