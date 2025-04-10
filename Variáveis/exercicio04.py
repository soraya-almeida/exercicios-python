#Peça o nome e a idade do usuário e exiba uma frase completa com essas informações.

nome = str(input("Informe o seu nome: "))
idade = int(input("Informe sua idade: "))

print("Você se chama", nome, "e tem", idade,"anos!")

#CORREÇÃO⬇️

nome = input("Nome: ")
idade = int(input("Idade: "))
print(f"{nome} tem {idade} anos.")
