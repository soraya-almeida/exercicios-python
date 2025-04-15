#Nota do aluno:
#Se a nota for maior ou igual a 7, exiba "Aprovado". Se for entre 5 e 6.9, exiba "Recuperação". Senão, exiba "Reprovado".

nota = float(input("Informe sua nota: "))

if nota >= 7:
    print(f"Você está APROVADO!")
elif nota >= 5:
    print(f"Você está em RECUPERAÇÃO!")
else:
    print(f"Você está REPROVADO!")