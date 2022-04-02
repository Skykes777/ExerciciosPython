frase = input('Digite uma frase: ').strip().lower()
letrasA = frase.count('a')
começaA = frase.find('a')+1
ultimoA = frase.rfind('a')+1
print(f'A frase: {frase}\ntem {letrasA} letras A, o primeiro a começa em {começaA} e termina em {ultimoA}. ')
