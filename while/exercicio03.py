#Senha até acertar
# Peça para o usuário digitar uma senha até que ele acerte a senha correta ("python123"). 
# Exiba uma mensagem de "acesso permitido" quando ele acertar.

senha = str(input("Informe a senha: "))

while senha != "python123":
    senha = str(input("Informe a senha: "))

print("Você acertou a senha!")