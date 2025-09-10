def converter_dolar_para_real(dolares, cotacao_dolar):
    reais = dolares * cotacao_dolar
    return reais

cotacao_dolar = 5.68
dolares = float(input("Digite o valor em dólares: "))
reais = converter_dolar_para_real(dolares, cotacao_dolar)

print(f"O valor de {dolares} dólares é igual a {reais:.2f} reais.")
