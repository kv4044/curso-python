from math import radians, sin, cos, tan
ang = float(input('Digite o angulo que voce deseja: '))
sin = sin(radians(ang))
print(f'O angulo de {ang} tem o SENO de {sin:.2f}')
cos = cos(radians(ang))
print(f'O angulo de {ang} tem o COSSENO de {cos:.2f}')
tan = tan(radians(ang))
print(f'O angulo de {ang} tem a TANGENTE de {tan:.2f}')
