#Peça uma senha duas vezes e imprima "Senha cadastrada com sucesso!" apenas se as duas forem iguais.

senha = input("Informe uma senha: ")
rep_senha = input("Informe a senha novamente: ")

if senha == rep_senha:
    print("Senha cadastrada com sucesso!")
else:
    print("As senhas precisam ser a mesma, tente novamente!")


