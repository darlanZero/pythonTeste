Real = float(input('Quanto dinheiro tem na carteira? '))
SellA = Real / 3.27
SellTo = Real / 5.00
print(f'Considerando que você tenha {Real} reais na sua carteira, você consegue comprar, em 2017, {SellA:=.3f} dol'
      f'áres. \n '
      f'Hoje, se compra {SellTo} doláres.')
