#Calcule a área de um círculo, pedindo o raio (float) e usando a fórmula: área = π * raio².

raio = float(input("Informe o raio do circulo: "))

area = 3.14159 * (raio ** 2)

print("A área do circulo com base no seu raio informado é", area)

#CORREÇÃO⬇️

import math
raio = float(input("Raio: "))
area = math.pi * raio ** 2
print("Área:", area)

