compra = list()

def vendas(produto, categoria, valor):
    while True:

        print("-"*100)
        print("VENDA")
        print("-"*100)

        produto = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        valor = float(input("Digite o valor do produto: "))

        
        compra.append(produto, categoria, valor)
        

        print("-"*100)
        continuar = input("Deseja continuar?(s/n): ").lower()

        if continuar == "n":
            break

print(vendas)