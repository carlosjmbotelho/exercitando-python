# Neste jogo o computador escolhe um número inteiro aleatório de 0 a 10, e o usuário tem 5 tentativas para adivinhar o número.
# Existe um sistema de pontuação com o seguinte comportamento: se o usuário adivinhar o número na primeira tentativa, receberá a pontuação máxima (100 pontos); se o usuário adivinhar o número na última tentativa, receberá a pontuação mínima (10 pontos); se o usuário não acertar o número, não receberá nenhum ponto.
# Há um controle de erros. Se o jogador digitar um número fora da faixa permitida ou caracteres não numéricos, o sistema notificará o jogador e solicitar o input correto.
# Há a opção de o usuário iniciar uma nova partida. Ao finalizar uma rodada, após o resultado final, o jogo irá perguntar se o jogador quer iniciar uma nova partida e, em caso negativo, encerra a aplicação.

from random import randint
from time import sleep

def linha():
    print('-=' * 25)
    
def separador():
    print('~~' * 20)
    
linha()
print(f'O computador escolheu um número de 1 a 10...'.center(50))
linha()

while True:
    fail = 1
    comp = randint(1, 10)
    while True:
        sleep(.5)
        while True:
            player = str(input('Qual número o computador escolheu? [Escolha entre 1 e 10] '))
            try:                  
                player = int(player)      
                if 0 < player < 11:
                    sleep(.5)
                    break
                else:
                    sleep(1)
                    separador()
                    print('Número \033[31mINVÁLIDO\033[m! Tente novamente!'.center(40))
                    separador()
                    sleep(1)
            except:
                sleep(1)
                print('\033[31mDigite apenas números!\033[m')
                sleep(.5)
        separador()
        if player == comp:
            sleep(.5)
            print(f'\033[34mVocê acertou após {fail} tentativas! Parabéns!\033[m')
            separador()
            break
        else:
            if fail < 5:
                sleep(.5)
                print('\033[31mVocê errou! Tente novamente!\033[m'.center(45))
                separador()
                fail += 1
            else:
                sleep(.5)
                print('\033[35mVocê esgotou suas tentivas!\033[m')
                print(f'O número escolhido pelo computador foi: {comp}.')
                fail = 0
                break
    sleep(.5)
    print('>> Sua pontuação foi: ', end='')
    if fail == 1:
        print('\033[34m100 pontos.\033[m')
    elif fail == 5:
        print('\033[33m10 pontos.\033[m')
    elif 1 < fail < 5:
        print('\033[33m50 pontos.\033[m')
    elif fail == 0:
        print('\033[31m0 pontos.\033[m')
    separador()
    while True:
        r = str(input('Jogar novamente [S/N]? ')).strip().upper()[0]
        sleep(.5)
        if r not in 'SN':
            separador()
            print('\033[31mOpção inválida! Tente com S ou N...\033[m')
            separador()
            sleep(1)
        elif r in 'SN':
            break
    if r == 'S':
        separador()
    elif r == 'N':
        linha()
        print('Ok! Até a próxima!'.center(50))
        linha()
        break

    