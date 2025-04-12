#Peça o nome e sobrenome do usuário, e crie um e-mail fictício no formato:
#"[nome].[sobrenome]@exemplo.com"

nome = input("Informe seu primeiro nome: ")
sobrenome = input("Informe seu sobrenome: ")

print(f"{nome}.{sobrenome}@gmail.com")

#CORREÇÃO⬇️

nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
email = f"{nome.lower()}.{sobrenome.lower()}@exemplo.com"
print("E-mail gerado:", email)
