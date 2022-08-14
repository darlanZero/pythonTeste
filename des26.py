fra = input('Escreva uma frase: ')
print(f'Quantas vezes aparece "A"?\n'
      f'Aparece {fra.count("a")} vezes\n'
      f'Em que posição aparece a letra a pela primeira vez?\n'
      f'Aparece pela primeira vez em {fra.find("a")}\n'
      f'Em que posição aparece a letra pela última vez?\n'
      f'Aparece pela ultima vez em {fra.rfind("a")}.')
