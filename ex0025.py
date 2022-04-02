nome = input('Digite o nome completo: ').strip()   #Colocando strip() para tirar os espaços vazios
lowernome = nome.lower()   #colocando todas as palavras em lower() 'minusculo' para padronizar o nome, mesmo que o usuario erre misturando minusculo com maiusculo
teste = 'silva' in lowernome   #irá procurar a palavra silva dentro de toda a frase que no caso é o nome completo
print(f'O seu nome tem Silva?: {teste}')