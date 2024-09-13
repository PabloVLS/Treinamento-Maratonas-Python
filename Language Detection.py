cont = 0
while True:
    s = input().strip()
    if s == "#":
        break
    else:
        cont += 1
        if s == "HELLO":
            print(f"Case {cont}: ENGLISH")
        elif s == "HOLA":
            print(f"Case {cont}: SPANISH")
        elif s == "HALLO":
            print(f"Case {cont}: GERMAN")
        elif s == "BONJOUR":
            print(f"Case {cont}: FRENCH")
        elif s == "CIAO":
            print(f"Case {cont}: ITALIAN")
        elif s == "ZDRAVSTVUJTE":
            print(f"Case {cont}: RUSSIAN")
        else:
            print(f"Case {cont}: UNKNOWN")
