ouro, prata, cobre = map(int, input().split())

total= (ouro*3) + (prata*2) + cobre

if total >= 8:
    print("Province or Gold")
elif total >=6:
    print("Duchy or Gold")
elif total >= 5:
    print("Duchy or Silver")
elif total >= 3:
    print("Estate or Silver")
elif total == 2:
    print("Estate or Copper ")
elif total == 1:
    print("Copper ")
else:
    print("Copper ")