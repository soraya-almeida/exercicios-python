#Número positivo ou negativo:
#Crie uma estrutura que diga se um número é positivo, negativo ou zero.

valor = float(input("Informe um número: "))

if valor > 0:
    print("Esse número é POSITIVO!")
elif valor == 0:
    print("Esse valor é ZERO!")
else:
    print("Esse número é NEGATIVO!")
