

while True:

    compra = [(produto, categoria, valor)]

    produto = input("Digite o nome do produto: ")
    compra.append(produto)
    categoria = input("Digite a categoria do produto: ")
    compra.append(categoria)
    valor = float(input("Digite o valor do produto: "))
    compra.append(valor)

    
    continuar = input("Deseja continuar?(s/n): ").lower()

    if continuar == "n":
        break

    print(compra)
    