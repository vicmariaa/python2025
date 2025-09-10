num=int(input("Digite o numero a ser convertido: \n"))
base=int(input('''escolha a base da conversao:
para binario digite 1
para octal digite 2
para hexadecimal digite 3
sua escolha: \n'''))
if base==1:
    print("conversao para binario")
    print("{} conevertido para binario é {}.".format(num, bin(num)[2:]))
elif base==2:
    print("conversao para octal")
    print("{} conevertido para octal é {}.".format(num, oct(num)[2:]))
elif base==3:
    print("conversao para hexadecimal")
    print("{} conevertido para hexadecimal é {}.".format(num, hex(num)[2:]))
else:
    print("Por gentileza só escolha apenas 1,2 e 3")