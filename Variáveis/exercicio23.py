#Peça um número ao usuário e mostre True se ele for negativo, False caso contrário.

num = int(input("Informe um número: "))

if num < 0:
    print(True)
else:
    print(False)

#CORREÇÃO⬇️

numero = float(input("Digite um número: "))
print("É negativo?", numero < 0)
