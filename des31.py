via = int(input('Qual a distância de um ponto à outro em km? '))
LimitViagem = int(200)
taxa1 = 0.50
taxa2 = 0.45
if via <= LimitViagem:
    print(f'Temos a taxa de R${taxa1} para viagens mais curtas, logo:')
    res1 = via * taxa1
    print(f'Você rodou {via} km de uma vez, logo, o preço da passagem é {res1:.2f}.')
else:
    print(f'Temos a taxa de R${taxa2}, para viagens mais longas, logo:')
    res2 = via * taxa2
    print(f'Você rodou {via} km de uma vez, logo, o preço da passagem é {res2:.2f}.')
