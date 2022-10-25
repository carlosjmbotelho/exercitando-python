# Verifica se um número inteiro é ou não um número primo. 
# Obs.: Um número primo é aquele que é divisível somente por ele mesmo e por 1.
# É explicitamente informado por quais números o número informado é divisível.

n = int(input('Digite um número: '))
mult = 0

for cont in range (1, n+1):
    if n % cont == 0:
        print(f'{n} é divisível por {cont}')
        mult += 1
if mult == 2:
    print(f'>>> {n} é divisível por {mult} números, logo É NÚMERO PRIMO!')
else:
    print(f'>>> {n} é divisível por {mult} números, logo NÃO É NÚMERO PRIMO!')