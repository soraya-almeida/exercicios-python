#Descubra o número secreto (fixo)
#Defina um número secreto no código. Peça que o usuário tente adivinhar até acertar.
#(Sem dica se é maior ou menor.)

numero = int(input("Adivinhe o número secreto: "))

while numero != 37:
    print("ERROU!")
    numero = int(input("Adivinhe o número secreto: "))
print("ACERTOU!")