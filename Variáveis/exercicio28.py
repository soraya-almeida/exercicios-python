#Peça um número e diga se ele é decimal (separado por ponto) ou inteiro (use float() e is_integer()).

Valor = float(input("Informe um número: "))

tipo = type(Valor)

print(tipo)

#CORREÇÃO⬇️

numero = float(input("Digite um número: "))
if numero.is_integer():
    print("É um número inteiro.")
else:
    print("É um número decimal.")
