def cal_total(idade, fidelidade, valor_total):
    desconto = 0
 
    if idade > 60:
        desconto += 10
 
    if fidelidade == True:
        desconto += 5
 
    valor_final = valor_total - (valor_total * desconto / 100)
    return valor_final
 
 
if __name__ == "__main__":
    print(cal_total(61, True, 300))