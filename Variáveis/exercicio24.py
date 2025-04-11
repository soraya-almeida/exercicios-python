#Peça nome, idade, peso e se pratica esportes (True/False), depois exiba todos os dados organizados.

nome = str(input("Informe seu nome: "))
idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
esporte = str(input("Pratica esporte: "))

print("Nome: ", nome)
print("Idade: ", idade)
print("Peso: ", peso)

if esporte == "Sim" or "s" or "S" or "sim":
    print("Pratica: True")
else:
    print("Pratica: False")

