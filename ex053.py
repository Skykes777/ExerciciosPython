frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Essa frase é um PALINDROMO!')
else:
    print('Eessa fras não é um PALINDROMO')
