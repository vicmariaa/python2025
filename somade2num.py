
num1 = int(input('Digite um numero a ser somado: '))
num2 = int(input('Digite o outro numero a ser somado: '))
total = num1 + num2
print('A soma entre {} e {} é igual a {}'.format(num1, num2, total))
print(f'A soma entre {num1} e {num2} é igual a {total}')

num1 = int(input('Digite um numero a ser subtraído: '))
num2 = int(input('Digite o outro numero a ser subtraído: '))
sub = num1 - num2
print(f'A subtração entre {num1} e {num2} é igual a {sub}')

num1 = int(input('Digite um numero a ser multiplicado: '))
num2 = int(input('Digite o outro numero a ser multiplicado: '))
mult = num1 * num2
print(f'A multiplicação entre {num1} e {num2} é igual a {mult}')

num1 = int(input('Digite um numero a ser dividido: '))
num2 = int(input('Digite o outro numero a ser dividido: '))
if num2 != 0:  # Verifica se o divisor não é zero
    div = num1 / num2
    print(f'A divisão entre {num1} e {num2} é igual a {div}')
else:
    print('Não é possível dividir por zero!')
