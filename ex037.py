numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{numero} convertido para binário é igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para octal é {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção invalida, tente novamente!')