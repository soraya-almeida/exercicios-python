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