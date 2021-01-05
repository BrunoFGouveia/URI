while True:
    try:
        n = int(input())
    except:
        break
    
    index=0
    pilha,fila,fila_p = [],[],[]
    stack,queue,priority=True,True,True

    for x in range(n):
        op, num = map(int, input().split())

        if op == 1:
            pilha.append(num)
            index+=1
            fila.append(num)
            fila_p.append(num)
            fila_p.sort(reverse=True)
        elif op == 2:
            if pilha[index-1] == num and stack:
                index-=1
                del pilha[index]
            else: stack=False

            if fila[0] == num and queue: del fila[0]
            else: queue=False

            if fila_p[0] == num and priority: del fila_p[0]
            else: priority=False

    if (stack and queue) or (stack and priority) or (queue and priority): print("not sure")
    elif stack: print("stack")
    elif queue: print("queue")
    elif priority: print("priority queue")
    else: print("impossible")