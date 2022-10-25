# Este programa mostra todos os números PRIMOS entre 1 e N, sendo N um número inteiro fornecido pelo usuário. 
# O programa deverá mostrar também a quantidade de números primos no intervalo.
# (PLUS) Há um controle do número digitado pelo usuário, forçando que este seja maior que ZERO.

while True:
    n = int(input('Listar os números primos até: '))
    cont = 0
    if n <= 0:
        print('Informar um valor maior que zero!')
    else:
        break        

print('Os números primos no intervalo solicitado são: ', end=" ")
for cont1 in range (1, n+1):    
    div = 0
    for cont2 in range (1, cont1+1):
        if cont1 % cont2 == 0:
            div += 1
        
    if div == 2:
        print(cont1, end=', ')
        cont += 1
print('FIM!')
print(f'\n>>> Há {cont} números primos no intervalo de 1 a {n}.')

    
        
        