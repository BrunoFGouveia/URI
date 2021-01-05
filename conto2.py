while 1:
    try:
        n,l,c = list(map(int, input().split(" ")))
        conto = input().split(" ")
        qtocaracter=0
        linhas=0
        paginas=0
        for x in range(len(conto)):
            qtocaracter += len(conto[x])
            if qtocaracter > c :
                linhas +=1
                qtocaracter = len(conto[x]) + 1
            elif qtocaracter == c:
                linhas +=1
                qtocaracter = 0 
            else:
                qtocaracter+=1
        if  qtocaracter>0 :
               linhas +=1                 
        paginas = linhas // l
        if linhas % l != 0:
            paginas += 1 
        print(paginas)
    except EOFError:
        break 