soma = 0
contador = 0
for c in range(1,7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        contador += 1
print(f'A soma de todos os {contador} numeros pares é  {soma}')
