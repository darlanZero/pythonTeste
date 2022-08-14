KM = int(input('Descreva a Km atual do seu veículo: '))
KmLimite = int(80)
Mul = int(7)
if KM > KmLimite:
    pro = (KM - KmLimite)
    print(f'Tendo seu carro {KM} Km,\n'
          f'Sua Multa será descontada nos seguintes Km excedentes: {pro} Km.')
    res = (pro * Mul)
    print(f'Sua multa resultante então será {res:.2f}.')
else:
    print(f'Tendo seu carro {KM} Km,\n'
          f'Parábens, passou pela multagem do detran!!')
