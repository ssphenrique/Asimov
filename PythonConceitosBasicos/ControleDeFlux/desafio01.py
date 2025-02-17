"""
Desafio: crie um programa que:
Pede por um nome de usuário e uma senha.
Se ambos forem corretos, exive uma mensagem de sucesso.
Caso contrário, exive uma mensagem de erro. A mensagem é diferente quando o usuário está incorreto, e quando a senha está incorreta
O usuário/senha "corretos podem ser definidos como variáveis dentro do próprio código.

"""
#Dados do cliente
usuario_correto = "pedro"
senha_correta = "123"

#Inputs de login
usuario = input("Digite seu nome de usuário: ") == usuario_correto
senha = input("Digite sua senha: ") == senha_correta

#Verificação de senha e usuario
if usuario and senha:
    print("Fazendo login")
elif not usuario and  senha:
    print("Usuário incorreto")
elif usuario and not senha:
    print("Senha incorreta")
else:
    print("Usuário e senha incorretos")
