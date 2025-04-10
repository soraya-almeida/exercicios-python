#Receba dois valores e troque os valores entre as variáveis, depois mostre o resultado.

valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))

valor_aux = valor1
valor1 = valor2
valor2 = valor_aux

print(valor1)
print(valor2)

#CORREÇÃO⬇️

a = input("A: ")
b = input("B: ")
a, b = b, a
print("A:", a)
print("B:", b)
