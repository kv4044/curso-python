times = ('Athletico-PR', 'Bahia', 'Bragantino', 'Botafogo', 'Flamengo', 'Sâo Paulo',
         'Internacional', 'Cruzeiro', 'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Grêmio',
         'Vasco da Gama', 'Juventude', 'Corinthians', 'Fluminense', 'Criciúma', 'Atlético-GO',
         'EC Vitória', 'Cuiabá')
print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os primeiros 5 são {times[:5]}')
print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabéticas: {sorted(times)}')
print('-='*20)
print(f'O Palmeiras está na {times.index("Palmeiras")+1}ª posição')
