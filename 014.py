def converter_unidades(valor_cm):
    metros = valor_cm / 100
    kilometros = valor_cm / 100000
    return metros, kilometros
valor_cm = float(input("Digite o valor em centímetros: "))
metros, kilometros = converter_unidades(valor_cm)
print(f"{valor_cm} cm é igual a {metros} metros e {kilometros} quilômetros.")
