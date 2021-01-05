import heapq
n, m = map(int, input().split())

v = list(map(int, input().split()))

itens = list(map(int, input().split()))

ans = 0
fila = []

for i in range(n):
    heapq.heappush(fila,(i,-i))

i=0
while i<m:                                                                              
    c = itens[i]
    i+=1
    p = heapq.heappop(fila)
    id = -p[1]
    l = p[0]+p[1]
    heapq.heappush(fila, ((l+v[id]*c)+id,-id))
    ans = max(ans, l+v[id]*c)

print(ans)