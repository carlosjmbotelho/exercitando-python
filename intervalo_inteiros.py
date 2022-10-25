# Este programa recebe dois números inteiros informados pelo usuário e gera os números inteiros que estão no intervalo dos números informados.

n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro inteiro: '))
soma = 0

def valores():
    print(f'Os valores inteiros entre {n1} e {n2} são: ', end='')

if n1 < n2:
    valores()
    for i in range (n1+1, n2):
        print(f'{i} -> ', end='')
        soma += i
    print('FIM!')
else:
    valores()
    for i in range (n1-1, n2, -1):
        print(f'{i} -> ', end='')
        soma += i
    print('FIM!')
        
print(f'\n>> A soma destes valores é: {soma}.')        
