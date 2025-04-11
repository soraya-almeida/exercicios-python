#Peça ao usuário uma frase e mostre quantas palavras ela tem (use .split()).

frase = str(input("Digite uma frase: "))

palavras = frase.split()
palavras_contador = len(palavras)

print("Está frase tem", palavras_contador, "palavras!")

#CORREÇÃO⬇️

frase = input("Digite uma frase: ")
palavras = frase.split()
print("Quantidade de palavras:", len(palavras))
