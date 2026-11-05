estoque = {"tomate": [1000, 2.30],
           "alface": [500, 0.45],
           "batata": [2001, 1.20],
           "feijão": [100, 1.50]}
prod = input(f"Produtos disponíves:\ntomate\nalface\nbatata\nfeijão ")
p2 = []
p2.append(prod)
venda = []
if prod in estoque:
    qt = int(input(f"{estoque[prod][0]} disponíveis: "))
    total = 0
    venda.append(p2)
    venda[0].append(qt)
    print("Vendas:\n")
    for operação in venda:
        produto, quantidade = operação
        preço = estoque[produto][1]
        custo = preço * quantidade
        print(f"{produto:12s}: {quantidade:3d} x {preço:6.2f} = {custo:6.2f}")
        estoque[produto][0] -= quantidade
        total += custo
    print(f" Custo total: {total:21.2f}\n")
    print("Estoque:\n")
    for chave, dados in estoque.items():
        print("Descrição: ", chave)
        print("Quantidade: ", dados[0])
        print(f"Preço: {dados[1]:6.2f}\n")
else:
    print("Produto não encontrado no estoque!")

