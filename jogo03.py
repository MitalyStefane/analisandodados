from random import randint
computador = randint(0, 10)
tentativas = 0
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Digite o número:'))
while jogador != computador:
    jogador = int(input('Hum... ERROU! Tente novamente:'))
    tentativas += 1
    if jogador < computador:
        print('Mais.. Tente novamente:')
    elif jogador > computador:
        print('Menos.. Tente novamente:')
print(f'Acertou com {tentativas}, pensei no número {computador}')