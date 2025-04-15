#Verificação de múltiplos:
#Diga se um número é múltiplo de 3, de 5, dos dois ou de nenhum.

numero = float(input("Informe um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("Esse número é multiplo de 3 e 5!")
elif numero % 5 == 0:
    print("Esse número é multiplo de 5!")
elif numero % 3 == 0:
    print("Esse número é multiplo de 3!")
else:
    print("Esse número não é multiplo de 3 e nem 5!")