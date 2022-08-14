import numbers
print('Bem-vindo ao Programa de elegibilidade dos números.')
n = int(input('vamos começar, descreva um numero: '))
ele = n % 2
if ele == 0:
    print(f'parábens, seu número é par!')
else:
    print('parábens, seu número é impar!')
