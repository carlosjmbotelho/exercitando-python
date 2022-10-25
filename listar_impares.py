# Imprime na tela apenas os números ímpares entre o número digitado pelo usuário e a base definida no programa.
# [PLUS] Controle do número digitado, forçando o usuário digitar um número ÍMPAR, número positivo e menor que a base.

base = 50

while True:
    num = int(input(f'Digite um número ÍMPAR, maior que ZERO e menor que {base}: '))    
    if num < 0:
        print(f'{num} é MENOR QUE ZERO. Tente novamente!')
    elif num > base:
        print(f'{num} é MAIOR que {base}. Tente novamente!')
    elif num == base:
        print(f'{num} é IGUAL a {base}. Tente novamente!')
    elif num % 2 == 0:
        print(f'{num} é PAR. Tente novamente!')
    else:
        print(f'>> Ímpares entre {num} e {base}: ')
        for i in range (num + 1, base):
            if i % 2 == 1:
                print(i, end=', ')
                i += 1
        print('FIM!')
        break
    
    