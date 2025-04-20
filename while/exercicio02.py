#Soma de números digitados
#Solicite ao usuário que digite números positivos. Some todos eles até que ele digite 0. Depois, exiba o total.

soma = 0
numero = int(input("Digite um número positivo para somar: (0 para sair)"))  

while numero != 0:
    soma += numero
    numero = int(input("Digite um número positivo para somar: ")) 

print(soma)
    
    