Pre = float(input('Preço total: '))
Desc = 0.05
SubPre = Pre * Desc
newPre = Pre - SubPre
print(f'Sabendo que seu preço é {Pre} \n e que tem 5% de desconto no preço \n o desconto é {SubPre:=.2f} '
      f'\n seu novo preço é {newPre:=.2f}.')
