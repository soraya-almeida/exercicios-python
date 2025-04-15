#Soma simples: Qual o resultado de 12 + 7?

print(12 + 7)

#Subtração: Qual o resultado de 50 - 23?

print(50 - 23)

#Multiplicação: Resolva 8 * 6.

print(8 * 6)

#Divisão comum: Quanto é 45 / 9?

print(45/9)

#Divisão inteira: Qual o resultado de 17 // 3?

print(17 // 3)

#Resto da divisão (módulo): Qual o valor de 17 % 3?

print(17 % 3)

#Potenciação: Resolva 2 ** 5.

print(2 ** 5)

#Expressão com vários operadores: Qual o resultado de 3 + 4 * 2? (Lembre da ordem das operações!)

print(3 + 4 * 2)

#Expressão com parênteses: Qual o valor de (3 + 4) * 2?

print((3 + 4) * 2)

#Desafio bônus: Um número é elevado ao quadrado, depois dividido por 3 (usando divisão inteira), e por fim somado ao resto da divisão dele por 3.
#Se o número for 10, qual é o resultado final?

num = float(input("Informe um número: "))
parte1 = num ** 2
parte2 = parte1 // 3
parte3 = num % 3

soma = parte2 + parte3
 
print("O resultado deu: ", soma)

