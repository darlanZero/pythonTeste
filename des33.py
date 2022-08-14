print('Bem-vindo à mais uma análise numérica!')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('dgite mais um número: '))
if n1 > n2 and n1 > n3:
    print(f'O maior valor é: {n1}')
else:
    if n2 > n1 and n2 > n3:
        print(f'O maior valor é: {n2}')
    else:
        if n3 > n1 and n3 > n2:
            print(f'O maior valor é: {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor número é: {n1}')
else:
    if n2 < n1 and n2 < n3:
        print(f'O menor número é: {n2}')
    else:
        if n3 < n1 and n3 < n2:
            print(f'O menor número é: {n3}')