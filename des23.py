num = input('Escreva um número de 0 à 9999: ')
jun = '000' + num
tam = len(jun)
print(f'unidade: {jun [tam-1]}\n'
      f'dezena: {jun [tam-2]}\n'
      f'centena: {jun [tam-3]}\n'
      f'milhar: {jun [tam-4]}\n')
