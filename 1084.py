while True:
    n = int(input())
    d = int(input())
    if n == 0 and d==0:
        break
    num = str(input())
    ls,apagados = [], []
    for i in range(n):
        numi = int(num[i])
        ls.append(numi)
        apagados.append(numi)
    apagados.sort()
    result = set(ls) - set(apagados[:d]) 
    print('{}'.format(str(result).replace("[","").replace("], ","\n").replace("]","").replace(",", "")))