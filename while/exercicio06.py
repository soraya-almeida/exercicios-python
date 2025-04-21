# Calcular média de notas
# Peça ao usuário para digitar várias notas. Pare quando ele digitar -1.
# Mostre a média (sem usar função).

nota1 = float(input("Informe uma nota: "))
nota2 = float(input("Informe outra nota: "))


while nota1 != -1 and nota2 != -1:
    print((nota1 + nota2)/2)
    nota1 = float(input("Informe uma nota: "))
    nota2 = float(input("Informe outra nota: "))

print("CABOOO")
