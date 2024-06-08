matiz = [[], [], []]
for l in range(0, 3):
    for c in range(0, 3):
        matiz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('=-' * 30)
for c in range(0, 3):
    print(f'{matiz[c]}')
