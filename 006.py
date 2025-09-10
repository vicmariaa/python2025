def preço (preço1):
    if preço1 >= 1000:
        return "Barato"
    else:
        return "Caro"
preço1 = float(input("Digite o valor do produto: "))
resultado = situacao(preço1)
print(f"O produto está {resultado}.")
