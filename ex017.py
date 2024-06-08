""" opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('comprimento do cateto adjacente: '))
hip = (opo ** 2 + adj ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hip:.2f}') """

from math import hypot
opo = float(input('Comprimento do cateto oposto: '))
adj = float(input('comprimento do cateto adjacente: '))
hip = hypot(opo, adj)
print(f'A hipotenusa vai medir {hip:.2f}')