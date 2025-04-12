#Peça dia, mês e ano separadamente, depois mostre a data no formato:
#"Você nasceu em DD/MM/AAAA."

nasceu = input("Informe sua data de aniversário: ")

from datetime import datetime
data_string = nasceu
data_datetime = datetime.strptime(data_string, "%d/%m/%Y")

print(data_string)