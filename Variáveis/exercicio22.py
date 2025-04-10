#Peça o valor de uma compra e o valor pago, depois mostre o valor do troco.

compra = float(input("Informe o valor da compra: "))
pago = float(input("Informe o valor pago: "))

troco = pago - compra

print("Seu troco é: ", troco)