#Peça uma temperatura em Celsius e converta para Fahrenheit usando a fórmula:

celsius = float(input("Informe uma temperatura em Celsius: "))

print("Convertido para Fahrnheit: ", (celsius * 1.8)+ 32)

#CORREÇÃO⬇️

celsius = float(input("Temperatura em °C: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}°C = {fahrenheit}°F")
