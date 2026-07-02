from f1 import cal_total

compra = list()


def cliente():
    print("-" * 100)
    print("FIDELIDADE E IDADE DO CLIENTE")
    print("-" * 100)

    fidelidade = input("Ele é fiel?(s/n): ").lower()
    idade = int(input("Digite a idade do cliente: "))

    return idade, fidelidade == "s"


def vendas():
    while True:
        print("-" * 60)
        print("VENDA")
        print("-" * 60)

        produto   = input("Digite o nome do produto: ").lower()
        categoria = input("Digite a categoria do produto: ").lower()
        valor     = float(input("Digite o valor do produto: "))

        compra.append({
            "produto":   produto,
            "categoria": categoria,
            "valor":     valor
        })

        print("-" * 60)
        continuar = input("Deseja continuar? (s/n): ").lower()

        if continuar == "n":
            break

    print("-" * 100)
    print("Vendas registradas:")
    for i, venda in enumerate(compra, start=1):
        print(f"  {i}. {venda['produto']} | {venda['categoria']} | R$ {venda['valor']:.2f}")


def main():
    idade, fidelidade = cliente()
    vendas()

    valor_total = sum(item["valor"] for item in compra)
    valor_final = cal_total(idade, fidelidade, valor_total)

    print("-" * 100)
    print("RESUMO DA COMPRA")
    print("-" * 100)
    print(f"Idade do cliente: {idade} anos")
    print(f"Cliente fiel: {'Sim' if fidelidade else 'Não'}")
    print(f"Valor total (sem desconto): R$ {valor_total:.2f}")
    print(f"Valor final (com desconto): R$ {valor_final:.2f}")


if __name__ == "__main__":
    main()