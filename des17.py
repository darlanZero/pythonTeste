import math
a = float(input('escreva aqui o cateto oposto: '))
b = float(input('escreva aqui o cateto adjacente: '))
c = math.hypot(a, b)
print(f'Então, o cateto da hipotenusa do triângulo retângulo\n'
      f'entre cateto oposto {a} e cateto adjacente {b} é {c:.2f}. ')