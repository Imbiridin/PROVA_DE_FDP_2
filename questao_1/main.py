compra = list()

def vendas():
    while True:
        print("-" * 60)
        print("VENDA")
        print("-" * 60)

        produto   = input("Digite o nome do produto: ")
        categoria = input("Digite a categoria do produto: ")
        valor     = float(input("Digite o valor do produto: "))

        
        compra.append({
            "produto":   produto,
            "categoria": categoria,
            "valor":     valor
        })

        print("-" * 60)
        continuar = input("Deseja continuar? (s/n): ").strip().lower()

        if continuar == "n":
            break   

    print("\nVendas registradas:")
    for i, venda in enumerate(compra, start=1):
        print(f"  {i}. {venda['produto']} | {venda['categoria']} | R$ {venda['valor']:.2f}")


if __name__ == "__main__":
    vendas()