sexo = input('Qual seu sexo? ')


if sexo == 'masculino':
    num1 = input('Digite sua altura: ')
    resultado = float(num1) * 72.7 - 58
    print('Seu peso ideal é: ', resultado, 'Kg')
if sexo == 'feminino':
    num1 = input('Digite sua altura: ')
    resultado = float(num1) * 62.1 - 44.7
    print('Seu peso ideal é: ', resultado, 'Kg')