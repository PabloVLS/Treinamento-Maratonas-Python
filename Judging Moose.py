a,b=map(int, input().split())

if a+b == 0:
    print("Not a moose")
else:
    if a==b:
        result=a+b
        print("Even",result)
    elif a!=b:
        if a>b:
            result = a*2
            print("Odd ", result)
        else:
            result = b*2
            print("Odd ", result)