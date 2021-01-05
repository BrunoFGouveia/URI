while 1:
    try:
        n,l,c = list(map(int, input().split(" ")))
        conto = input().split(" ")
        qtocaracter=0
        linhas=0
        linha = ""
        paginas=0
        for x in range(0, len(conto), 1):
            linha += conto[x]
            print(linha) 
            if len(linha) > c:
                linhas +=1
                linha = conto[x] + " "                
            elif len(linha) == c:
                linhas +=1
                linha = ""
            elif x!= len(conto):
                linha += " "

        if  len(linha)>0 :
               linhas +=1                 
        paginas = linhas // l
        if linhas % l != 0:
            paginas += 1 
        print(linha)
        print(linhas,paginas)
    except EOFError:
        break 