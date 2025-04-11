#Peça um número e um texto, e mostre os dois juntos em uma frase como: "Você digitou o número X e a palavra Y".

num = int(input("Informe um número: "))
car = str(input("Informe uma palavras: "))

print("Você digitou o número", num, "e a palavras", car)

#CORREÇÃO⬇️

numero = input("Digite um número: ")
palavra = input("Digite uma palavra: ")
print(f"Você digitou o número {numero} e a palavra {palavra}.")
