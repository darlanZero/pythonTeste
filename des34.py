print('aumento Salarial\n'
      'primeiramente, saiba que Pessoas com salários superiores à 1250,00 ganham 10% de aumento\n'
      'E, pessoas com salários  inferiores à 1250,00 têm aumento de 50%.')
Sal = float(input('Tendo em vista as informações acima, qual seu salário atual? '))
if Sal <= 1250.00:
    Aum1 =float(1.15)
    Res1 = Sal * Aum1
    print(f'Seu salário sendo de {Sal}, logo, seu salário aumenta 15%.\n'
          f'Com isso, seu salário se torna {Res1:.2f}.')
else:
    Aum2 = float(1.10)
    Res2 = Sal * Aum2
    print(f'Seu salário sendo de {Sal}, logo, seu salário aumenta 10%.\n'
          f'Com isso, seu salário se torna {Res2:.2f}.')
