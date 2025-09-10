# EX: 022 - Somar apenas os números pares digitados pelo usuário

# Inicializa a variável 's' com 0, que vai armazenar a soma dos números pares
s = 0

# Inicia um laço que vai repetir 6 vezes (de 0 a 5)
for i in range(0, 6):

    # Solicita que o usuário digite um número e converte para inteiro
    num = int(input("Digite um número: \n"))

    # Verifica se o número digitado é par
    if num % 2 == 0:
        # Se for par, soma o número com a variável 's'
        s += num

# Após o laço, exibe o resultado da soma dos números pares digitados
print("Somas: {}.".format(s))
