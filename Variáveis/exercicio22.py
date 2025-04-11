#Peça o valor de uma compra e o valor pago, depois mostre o valor do troco.

compra = float(input("Informe o valor da compra: "))
pago = float(input("Informe o valor pago: "))

troco = pago - compra

print("Seu troco é: ", troco)

#CORREÇÃO⬇️

compra = float(input("Valor da compra: R$"))
pago = float(input("Valor pago: R$"))
troco = pago - compra
print(f"Troco: R${troco:.2f}")
