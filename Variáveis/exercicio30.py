#Peça ao usuário para digitar "sim" ou "não", e transforme isso em um valor booleano (True para "sim", False para "não").

palavra = str(input("Informe sim ou não: "))

resultado = palavra == "sim"

print(resultado)

#CORREÇÃO⬇️

resposta = input("Digite 'sim' ou 'não': ").strip().lower()
booleano = resposta == "sim"
print("Valor booleano:", booleano)
