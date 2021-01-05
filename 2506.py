while True:
    try:
        n = int(input())
    except:
        break
 
    ans = 0
    tempo_total = 420
    for i in range(n):
        h,m,c =  map(int, input().split())
        while (tempo_total < (h * 60) + m):
            tempo_total += 30
            
        if (tempo_total - ((h * 60) + m) > c):
            ans+=1

        tempo_total += 30
    print(ans)
