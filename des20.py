import  random
al1 = input('Nome do 1° aluno: ')
al2 = input('Nome do 2° aluno: ')
al3 = input('Nome do 3° aluno: ')
al4 = input('Nome do 4° aluno: ')
alunos = al1, al2, al3, al4
ord = random.sample(alunos, 4)
print(f'tendo o professor querendo sortear a ordem de apresentação do trabalho,\n'
      f'ele decide sortear entre os alunos {al1}, {al2}, {al3}, {al4}.\n'
      f'A ordem sorteada é {ord}.')