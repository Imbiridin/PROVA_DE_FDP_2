compra = list()

pessoa = list()

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

    print("-"*100)
    print("Vendas registradas:")
    for i, venda in enumerate(compra, start=1):
        print(f"  {i}. {venda['produto']} | {venda['categoria']} | R$ {venda['valor']:.2f}")


if __name__ == "__main__":
    vendas()


def cliente():
    
    while True:
        
        print("-"*100)
        print("FIDELIDADE E IDADE DO CLIENTE")
        print("-"*100)

        fidelidade = input("Ele é fiel?(s/n): ").lower()
        idade = int(input("Digite a idade do cliente: "))


        pessoa.append({
            "fidelidade": fidelidade,
            "idade": idade
        })
        
        print("-"*100)
        continuar = input("Deseja continuar?(s/n): ").lower()

        if continuar == "n":
            break

    print("-"*100)
    print("CLIENTES CADASTRADOS")
    print("-" * 60)
    for i, c in enumerate(pessoa, start=1):
        fiel = "Sim" if c["fidelidade"] == "s" else "Não"
        print(f"  {i}. Fidelidade: {fiel} | Idade: {c['idade']} anos")

if __name__ == "__main__":
    cliente()


