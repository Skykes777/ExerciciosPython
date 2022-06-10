def função():
    global n1
    n1 = 4
    print(f'N1 dentro da função vale {n1}')
# -Escopo local


# -Escopo global
n1 = 2
função()
print(f'N1 fora(programa principal) vale {n1}')
