#Validação de nota
# Peça ao usuário uma nota de 0 a 10. Continue pedindo até que ele digite um valor válido.

nota = int(input("Informe uma nota de 0 a 10: [Digite 14 para parar!]"))

while nota != 14:
    print(f"Nota {nota}")
    nota = int(input("Informe uma nota de 0 a 10: [Digite SAIR para parar!]"))

    print("Sessão Finalizada!")


