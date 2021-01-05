while True:
    n = int(input())
    if n == 0:
        break
    while True:
        entrada = list(map(int, input().split()))
        if entrada[0] == 0:
            print('')
            break
        p = []
        curr = 0
        for i in range(1,n+1):
            p.append(i)
            while len(p)>0 and entrada[curr] == p[len(p)-1]:
                curr+=1
                p.pop()

        if len(p)==0:
            print('Yes')
        else:
            print('No') 