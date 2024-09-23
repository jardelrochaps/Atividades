num1 = input('Digite um número inteiro: ')
num2 = input('Digite outro número inteiro: ')
num3 = input('Digite um número real: ')

if num1.isdigit() and num2.isdigit():
    resultado1 = (int(num1) * 2 ) + (int(num2) / 2)
    resultado2 = (int(num1) * 3 ) + (float(num3))
    resultado3 = (float(num3) ** 3)

    print('o produto do dobro do primeiro com metade do segundo: ',resultado1)
    print('a soma do triplo do primeiro com o terceiro: ',resultado2)
    print('o terceiro elevado ao cubo: ',resultado3)
else:
    print('Há algo de errado!')