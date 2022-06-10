from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'Contando de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont, end=' ', flush=True)
            sleep(0.3)
            cont -= p
        print('FIM!')
# -Função de contagem com escolha 


# -Programa principal
contador(10, 1, 1)
contador(10, 0, 2)
print('-='*20)
print()
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
