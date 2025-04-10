#Peça a altura e o peso do usuário e mostre o IMC (peso / altura²).

altura = float(input("Informe sua altura: "))
peso = float(input("Informe o seu peso: "))

imc = peso / (altura ** 2)

print("O seu IMC é", imc)