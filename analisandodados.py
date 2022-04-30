print('-' * 20)
print('CADASTRO DE PESSOAS')
print('-' * 20)
total = total1 = total2 = total3 = 0
while True:
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('-' * 20)
    total += 1
    if idade >= 18:
        total1 += 1
    if sexo == 'M':
        total2 += 1
    if sexo == 'F' and idade < 20:
        total3 += 1
    opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-' * 20)
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        print('-' * 20)
    if opcao == 'N':
        break

print(f'Total de pessoas maiores de idade: {total1}')
print(f'Ao todo temos {total2} homens cadastrados')
print(f'Temos {total3} mulheres com menos de 20 anos')