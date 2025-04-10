#Peça o nome de um produto e o seu preço (float), depois mostre uma frase com os dois.

produto = str(input("Informe o nome do produto: "))
preco = float(input("Informe o valor do produto: "))

print("O seu produto é", produto, "e o preço é", preco, ".")

#CORREÇÃO⬇️

produto = input("Produto: ")
preco = float(input("Preço: "))
print(f"O produto {produto} custa R${preco:.2f}")
