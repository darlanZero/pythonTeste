Alt = float(input('Qual a altura da parede? '))
Lar = float(input('Qual a largura da parede? '))
Ar = Alt * Lar
QuantTinta = float(Ar / 2)
print(f'Sendo que a parede mede {Alt} por {Lar}, logo, sua área é {Ar}, e é necessário {QuantTinta} litros para '
      f'preencher a '
      f'parede.')
