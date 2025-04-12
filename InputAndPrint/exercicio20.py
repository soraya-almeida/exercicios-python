#Peça uma frase ao usuário e mostre ela em:
#Letras maiúsculas
#Letras minúsculas
#Número de caracteres (sem contar espaços)

frase = input("Informe uma frase completa: ")

maiuscula = frase.upper()
print(maiuscula)

minuscula = frase.lower()
print(minuscula)

quantidade = len(frase)
print(quantidade)

#CORREÇÃO⬇️

frase = input("Digite uma frase: ")
print("Maiúsculas:", frase.upper())
print("Minúsculas:", frase.lower())
print("Total de letras (sem espaços):", len(frase.replace(" ", "")))
