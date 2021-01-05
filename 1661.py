i = 0
while True:
    n = int(input())
    if n == 0:
        break
    ls = list(map(int, input().split()))
    

    resp,carrega = 0,0 

    for i in range(len(ls)):
        carrega+=ls[i]


        if carrega>0:
            resp += carrega
        else:
            resp += -1 * carrega
        

    print(resp)
                 