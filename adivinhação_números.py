# Neste jogo o computador escolhe um número aleatoriamente entre 1 e 50.
# O jogador (usuário) tentará adivinhar qual número o computador escolhendo, obtendo dicas a cada tentativa.
# Ao final, é exibido a quantidade de tentativas que o jogador precisou para acertar o número.

from random import randint
from time import sleep

comp = randint(1, 50)
tent = 1

def linha():
    print('-=' * 30)
    
linha()
print(f'\033[35m{"JOGO DE ADIVINHAÇÃO":^60}\033[m')

while True:
    linha()
    user = int(input('>> Qual número o computador escolheu? '))
    linha()
    if user == comp:
        print(f"\033[34m{'*** Você ACERTOU! PARABÉNS! ***':^60}\033[m")
        linha()
        sleep(1)
        break
    elif user < comp:
        print('\033[31mVocê ERROU! Suba mais um pouco...\033[m')
        sleep(1) 
    elif user > comp:
        print('\033[31mVocê ERROU! Desça mais um pouco...\033[m')
        sleep(1)
    tent += 1
        
print(f'Você precisou de {tent} tentativas para acertar.'.center(60))
linha()