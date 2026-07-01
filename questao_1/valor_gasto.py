compras = [

    ("Banana", "fruta", 8.50),

    ("Arroz", "mercado", 25.00),

    ("Tomate", "verdura", 12.00),

    ("Sabão", "limpeza", 18.00)

]

def valor_gasto(compras):
    total = 0
    for item in compras:
        categoria = item[1]
        if categoria == "fruta" or categoria == "verdura":
            total += item[2]
    return total

if __name__ == "__main__":
    total = valor_gasto(compras)
    print(f"Valor total gasto em hortifrúti: R${total:.2f}")
