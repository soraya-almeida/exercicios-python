#Calculadora simples:
#Peça dois números e uma operação (+, -, *, /) e retorne o resultado.

num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))
print("Você quer qual operação⬇️")
print("[+] ADIÇÃO")
print("[-] SUBTRAÇÃO")
print("[*] MULTIPLICAÇÃO")
print("[/] DIVISÃO")

operacao = str(input("Escolha um sinal: "))

if operacao == "+":
    print(num1 + num2)
elif operacao == "-":
    print(num1 - num2)
elif operacao == "*":
    print(num1 * num2)
elif operacao == "/":
    print(num1 / num2)