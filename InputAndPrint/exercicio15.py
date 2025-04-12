#Peça três letras e quatro números separadamente, depois exiba:
#"Placa: ABC-1234"

letra = input("Informe 3 letras: ")
numeros = input("Informe 4 números: ")

print(f"Placa: {letra}-{numeros}")

#CORREÇÃO⬇️

letras = input("Digite as 3 letras da placa: ")
numeros = input("Digite os 4 números da placa: ")
print(f"Placa: {letras.upper()}-{numeros}")
