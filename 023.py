# EX: 021 - Mostrar todos os números pares de 1 a 50

# Inicia um laço que percorre os números de 1 até 50 (o 51 não está incluso)
for num in range(1, 51):

    # Verifica se o número atual é par (ou seja, divisível por 2)
    if num % 2 == 0:
        # Se for par, imprime o número
        print(num)
