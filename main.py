nume = int(input("Entre com um numero: "))

for x in range(1, nume+1, 1):
    if (nume%x == 0):
        print(x)


