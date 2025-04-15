#Maior entre 3 números:
#Receba três números e diga qual é o maior entre eles.

num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
num3 = int(input("informe outro número: "))

if num1 > num2 and num1 > num3:
    print("O primeiro valor é MAIOR que o segundo e o terceiro valor!")
elif num2 > num1 and num2 > num3:
    print("O segundo valor é MAIOR que o primeiro e o terceiro valor!")
else:
    print("O terceiro valor é MAIOR que o primeiro e o segundo valor!")