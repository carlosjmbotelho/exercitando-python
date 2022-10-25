# Programa para armazenar quatro notas em uma lista e apresentar a média final.
# Caso a média seja igual ou superior a 7, apresentará a mensagem "APROVADO". Caso contrário, o aluno fará prova de recuperação e armazenará a nota da prova no programa que recalculará a média. 
# Caso a nova média seja igual superior a 5, apresentará a mensagem "APROVADO", caso contrário, apresentará a mensagem "REPROVADO".

notas = []
contador = 1

while contador < 5:
    notas.append(float(input(f'Digite a Nota {contador}: ')))
    contador += 1
    
media = sum(notas) / len(notas)
    
print(f'A média do aluno foi: {media}', end='')
if media >= 7:
    print('. \nAluno APROVADO!')
else:
    notas.append(float(input('\nDigite a Nota de Recuperação: ')))
    media = sum(notas) / len(notas)
    print(f'A média final do aluno em recuperação foi: {media}', end='')
    if media >= 5:
        print('. \nAluno APROVADO na recuperação!')
    else:
        print('. \nAluno REPROVADO!') 