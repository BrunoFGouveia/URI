while True:
    try:
        entrada = input()
        resp = True
        p1,p2= 0,0
        pr,ul = "",""
        for x in entrada:
            if (x == '('):
                p1 += 1
                ul = x
                if pr == '':
                    pr = x
            elif (x == ')'):
                p2 += 1
                ul = x
                if pr == '':
                    pr = x
                

        if((p1+p2)%2 != 0):
            resp = False
        else:
            if(pr == ')'):
                resp = False
            else:
                if (ul == '('):
                    resp = False
                else:
                    if (p1 != p2):
                        resp = False
                
        if(resp):
            print("correct")
        else:
            print("incorrect")

    except (EOFError):
        break