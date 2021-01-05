ls = []
n = int(input())
for i in range(n):
    input()
    alt = list(map(int, input().split()))
    alt.sort()
    ls.append(alt)


print('{}'.format(str(ls).replace("[","").replace("], ","\n").replace("]","").replace(",", "")))