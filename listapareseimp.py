valor = [[], []]
v = 0
for c in range(1, 8):
    v = int(input(f'Digite o {c} valor:'))
    if v % 2 == 0:
        valor[0].append(v)
    else:
        valor[1].append(v)
print(f'Os valores pares são {valor[0]}')
print(f'Os valores impares são {valor[1]}')


