#Sistema de login simples:
#Peça um nome de usuário e senha. Se os dois estiverem corretos, exiba “Acesso permitido”.
#Caso contrário, exiba “Acesso negado”.

usuario = "sol14"
senha = 1111214

qual_usuario = str(input("Informe seu nome de usuário: "))
qual_senha = int(input("Informe sua senha: "))

if (qual_usuario == usuario) and (qual_senha == 111214):
    print("Acesso permitido.")
else:
    print("Acesso negado.")