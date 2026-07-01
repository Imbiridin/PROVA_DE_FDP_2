def calcular_valor_total(compras):
    
    total = 0.0
    for produto, categoria, valor in compras:
        total += valor
    return total


def calcular_valor_frutas_verduras(compras):
   
    total_f_v = 0.0
    for produto, categoria, valor in compras:
        if categoria in ("fruta", "verdura"):
            total_f_v += valor
    return total_f_v


def calcular_percentual_desconto(valor_total, valor_frutas_verduras, cliente_fidelidade, idade_cliente):

    desconto = 0

   
    if idade_cliente > 60:
        desconto += 10

    
    if cliente_fidelidade:
        desconto += 5

    
    if valor_frutas_verduras > 30.00:
        desconto += 5

   
    if desconto > 20:
        desconto = 20

    return desconto


def exibir_resumo(compras, cliente_fidelidade, idade_cliente):
    
    valor_original = calcular_valor_total(compras)
    valor_frutas_verduras = calcular_valor_frutas_verduras(compras)
    desconto_percentual = calcular_percentual_desconto(
        valor_original, valor_frutas_verduras, cliente_fidelidade, idade_cliente
    )
    
    
    valor_desconto = valor_original * (desconto_percentual / 100)
    valor_final = valor_original - valor_desconto

    print("===== RESUMO DA COMPRA =====")
    print(f"Valor original: R$ {valor_original:.2f}")
    print(f"Valor de frutas e verduras: R$ {valor_frutas_verduras:.2f}")
    print(f"Desconto aplicado: {desconto_percentual}%")
    print(f"Valor final: R$ {valor_final:.2f}")
    print("==========================================================")



if __name__ == "__main__":
    compras = [
        ("Banana", "fruta", 8.50),
        ("Arroz", "mercado", 25.00),
        ("Tomate", "verdura", 12.00),
        ("Sabão", "limpeza", 18.00)
    ]
    cliente_fidelidade = True
    idade_cliente = 67

    exibir_resumo(compras, cliente_fidelidade, idade_cliente)
