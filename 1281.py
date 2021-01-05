n = int(input())
for i in range(n):
    produtos = {}
    soma = 0
    qtd_produtos = int(input())
    for j in range(qtd_produtos):
        produto = input().split()
        produtos[produto[0]] = float(produto[1])

    qtd_compra_produto = int(input())

    for l in range(qtd_compra_produto):
        compras = input().split()
        if compras[0] in produtos:
            soma += produtos[compras[0]] * int(compras[1]) 
    
    print('R$ {:.2f}'.format(soma))