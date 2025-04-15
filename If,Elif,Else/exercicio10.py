#Desafio de desconto:
#Se o cliente comprar acima de R$100, aplique 10% de desconto. 
#Se for entre R$50 e R$99, aplique 5%. Senão, sem desconto. Mostre o valor final.

compra = float(input("Informe o valor da sua compra: "))

desconto10 = (compra * 10)/ 100
desconto5 = (compra * 5)/ 100

if compra > 100:
    print("Você recebeu um desconto de 10%!😎 Portanto o valor da sua compra é", compra - desconto10)
elif compra >= 50 and compra <= 99:
    print("Você recebeu um desconto de 5%!😊 Portanto o valor da sua compra é", compra - desconto5)
else:
    print("Você não recebeu desconto nenhum!☹️")