# Programa para ler nome de usuário e senha. 
# Caso a senha seja igual ao nome do usuário, tenha a mesma quantidade ou menor em caracteres, é mostrado uma mensagem de erro e volta a pedir as informações.

from time import sleep


while True:
    nome = str(input('Nome de usuário: '))
    senha = str(input('Senha: '))
    if senha != nome and len(senha) > len(nome):
        break
    else:
        print('\033[31mSenha não pode ser igual ou menor que nome de usuário!\033[m')
        sleep(1)
        print('Tente novamente!')
        sleep(.5)

print('Tudo ok')
