#Mostre só as palavras com mais de 5 letras:
#Ignore as curtinhas e imprima só as grandes.

cores = ["Azul", "Amarelo", "Vermelho"]

for cor in cores:
    if len(cor) == 5:
        print("Sua cor", cor)
