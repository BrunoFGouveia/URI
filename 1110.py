while True:
    n = int(input())
    if n == 0 :
        break

    remaining = []
    for x in range(n):
        remaining.append(x+1)

    discarded = []
    while len(remaining) > 1:
        discarded.append(remaining.pop(0))
        remaining.insert(len(remaining)-1,remaining.pop(0))

    print('Discarded cards: {}'.format(str(discarded).replace("[","").replace("]","")))
    print('Remaining card: {}'.format(remaining[0]))