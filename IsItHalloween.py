data = input()
mes,dia=data.split()
dia = int(dia)
if mes == "OCT" and dia==31:
    print("yup")
elif mes=="DEC" and dia==25:
    print("yup")
else:
    print("nope")
