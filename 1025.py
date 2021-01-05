from bisect import bisect_left

i = 0
while True:
    n, q = map(int, input().split())
    if n == q == 0:
        break
    i += 1
    marmore = []
    for x in range(n):
        marmore.append(int(input()))
    marmore.sort()
    print('CASE# {}:'.format(i))
    for x in range(q):
        num = int(input())
        index = (bisect_left(marmore, num))
        if index < len(marmore) and marmore[index] == num:
            print('{} found at {}'.format(num, index+1))
        else:
            print('{} not found'.format(num))        