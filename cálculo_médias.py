# Programa para armazenar quatro notas em uma lista e apresentar: a média final, a maior nota e a menor nota.

notas = []
quant = 0

for i in range (1, 5):
    notas.append(float(input(f'Digite a Nota {i}: ')))
    quant += 1    
    
media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

print(f'A média das {quant} notas digitadas foi {media}.')   
print(f'A maior nota foi {maior}.')
print(f'A menor nota foi {menor}.')
