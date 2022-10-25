# Utilizando a Função Lambda, criei uma calculadora rudimentar onde o usuário deve informar: os valores para a realização do cálculo (apenas dois valores), qual operação ele deseja realizar e o resultado da operação.
# Com Lambda isso é feito de forma simples e objetiva.

print('** CALCULADORA - LAMBDA **')

n1 = int(input('Digite o 1º número para calcular: '))
n2 = int(input('Digite o 2º número para calcular: '))

opcao = int(input(
''' \n*** OPERAÇÃO ARITMÉTICA ***
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão

Digite a operação que deseja: '''))

if opcao == 1:
    operacao = 'Adição'
    result = lambda x: n1 + n2
elif opcao == 2:
    operacao = 'Subtração'
    result = lambda x: n1 - n2
elif opcao == 3:
    operacao = 'Multiplicação'
    result = lambda x: n1 * n2
elif opcao == 4:
    operacao = 'Divisão'
    result = lambda x: n1 / n2
    
print('*' * 30)
print(f'O resultado da {operacao} é: {result(opcao)}')
print('*' * 30)