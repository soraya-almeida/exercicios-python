#Peça ao usuário dois números e diga qual é o maior.

num1 = int(input("Informe um valor: "))
num2 = int(input("Informe outro valor: "))

if num1 > num2:
    print("O primeiro valor é maior que o segundo valor!")
else:
    print("O segundo valor é maior que o segundo valor!")

#CORREÇÃO⬇️

a = float(input("Número 1: "))
b = float(input("Número 2: "))
print("Maior número:", max(a, b))
