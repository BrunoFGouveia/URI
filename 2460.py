n = int(input())
fila = list(map(int, input().split()))

m = int(input())
rb = list(map(int, input().split()))
pos = 0
for i in range(m):
    pos = fila.index(rb[i])
    del(fila[pos])


print('{}'.format(str(fila).replace("[","").replace("]","").replace(",", "")))