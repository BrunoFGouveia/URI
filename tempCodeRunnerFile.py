while True:
    n,d = map(int, input().split())
    if n == 0 and d==0:
        break
    num = input()
    ls,apagados = [], []
    for i in range(n):
        numi = int(num[i])
        ls.append(numi)
        apagados.append(numi)
    apagados.sort()
    result = set(ls) - set(apagados[d:]) 
    print('{}'.format(str(result).replace("[","").replace("], ","\n").replace("]","").replace(",", "")))