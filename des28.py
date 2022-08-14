import random

print('olá Usuário!\n'
      'Bem Vindo ao jogo de Adivinhação da Máquina!\n'
      'Basicamente, a maquina escolherá um número de 0 a 5, e tudo que tem que fazer é acertar.\n'
      'Okay? Vamos lá!')
num = 0, 1, 2, 3, 4, 5
numEscolhido = random.choice(num)
Resp = int(input('Escreva aqui sua resposta, participante:'))
if Resp == numEscolhido:
    print(f'parábens, você passou!')
else:
    print('não foi dessa vez, tente na próxima!')
print(f'O número escolhido pela máquina é {numEscolhido}.')
