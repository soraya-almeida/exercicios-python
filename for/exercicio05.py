#Verifique se a palavra tem a letra "a":
#Pra cada palavra, diga se ela tem a letra "a" dentro.

#len() - quantidade dem numero
#count() - contagem de palavras ou letras especificas

colors = ["Yellow", "Blue", "Red", "Green", "Black"]

for color in colors:
    contagem = color.count("a")
    print("A palavra", color, "tem", contagem), "letras A!"