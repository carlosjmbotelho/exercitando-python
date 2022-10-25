# Programa para informar a quantidade de números inteiros, calcular e mostrar a quantidade de números pares e a quantidade de números ímpares no intervalo.

par = impar = 0
base = 20

for i in range (1, base + 1):
    numero = int(input(f'Digite o {i}º número: '))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
        
print(f'Foram digitados {par} números pares e {impar} números ímpares.')
    
    