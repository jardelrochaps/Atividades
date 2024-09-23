peso = input('Qual o peso dos peixes? ')


if float(peso) > 50:
    resultado = (float(peso) - 50) * 4
    print('Sua multa é de: %.2f'%resultado, 'Reais')

else:
    print('Você não foi multado!')