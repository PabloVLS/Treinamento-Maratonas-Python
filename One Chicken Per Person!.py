p,f = map(int, input().split())

if p > f:
    result = p-f
    if result == 1:
        print("Dr. Chaz needs",result, "more piece of chicken!")
    else:
        print("Dr. Chaz needs", p-f ,"more pieces of chicken!")
else:
    result = f-p
    if result == 1:
        print("Dr. Chaz will have", result, "piece of chicken left over!")
    else:
        print("Dr. Chaz will have",f-p , "pieces of chicken left over!")