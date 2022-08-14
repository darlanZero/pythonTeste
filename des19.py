import random
al1 = input('Escreva aqui o nome de 1 aluno: ')
al2 = input('Escreva aqui o nome de seu 2° aluno: ')
al3 = input('Escreva aqui o nome do seu 3° aluno: ')
al4 = input('Escreva aqui o nome do seu 4° aluno: ')
alunos = al1, al2, al3, al4
es = random.choice(alunos)
print(f'Entre os alunos {al1}, {al2}, {al3}, {al4}, você, professor\n'
      f'Escolheu o aluno {es}.')