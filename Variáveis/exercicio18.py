#Peça um número inteiro e diga se ele é positivo, negativo ou zero.

num = int(input("Informe um número: "))

if num >= 1:
    print("Esse número é positivo!")
elif num == 0:
    print("Esse número é zero!")
else:
    print("Esse valor é negativo!")

#CORREÇÃO⬇️

numero = int(input("Digite um número: "))
if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Zero")
