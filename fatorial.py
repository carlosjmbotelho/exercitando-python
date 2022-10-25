# Calcula o fatorial do número informado pelo usuário.
# O programa permite ao usuário calcular o fatorial várias vezes e limita o fatorial a números inteiros positivos e menores que 16.

while True:
    n = int(input('Fatorial de: '))
    if n > 16:
        print('ERRO! Número apenas até 16!')
    elif n < 0:
        print('ERRO! Não existe fatorial de número negativo!')
    else:
        fatorial = 1
        print(f'{n}! -> {n}', end='')
        for i in range (n, 1, -1):
            fatorial *= i 
            print(f'x{i-1}', end='')
        print(f' = {fatorial}.')
        while True:
            r = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
            if r in 'SN':
                break
            print('ERRO! Tente novamente! Apenas S ou N.')
        if r == 'N':
            print('Volte sempre!')
            break

        