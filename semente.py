f,r = list(map(int, input().split(" ")))
p = list(map(int, input().split(" ")))
l=[]
dias = 0
qtd = 0
l = [0 for x in range(0,f)]
while qtd<f:
    dias +=1
    for y in range(0,r,1):        
        if dias==1:
            l[p[y]-dias]=1
            qtd+=1
        else:
            if p[y]-dias >= 0 and l[p[y]-dias]==0:
                l[p[y]-dias]=1
                qtd+=1
            if p[y]+dias-2 < f and l[p[y]+dias-2]==0:
                qtd+=1
                l[p[y]+dias-2]=1    

print(dias-1)