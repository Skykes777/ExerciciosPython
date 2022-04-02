n = contador = 0
todos_números = []
controle = ''
while controle != 'N':
    n = int(input('Digite um número: '))
    todos_números.append(n)
    contador += 1
    controle = input('Deseja cotinuar? [S/N]: ').strip().upper()
media = sum(todos_números) / contador
maior_valor = max(todos_números)
menor_valor = min(todos_números)
print(f'''Você digitou {contador} números, e a média foi {media :.2f}
O maior número foi {maior_valor}, e o menor valor foi {menor_valor}.''')
