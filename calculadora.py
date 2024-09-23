operacoes = ['+', '-', '/', '*']
resultado = 0


print('Bem vindo a calculadora!')

nome = input('Digite seu nome: ')

num1 = input('Digite o 1° valor: ')
num2 = input('Digite o 2° valor: ')

operacao = input('Qual dessas ' + str(operacoes) + ' operações você deseja? ')

if operacao in operacoes:
    if num1.isdigit() and num2.isdigit():
        if operacao == '+':
           resultado = int(num1) + int(num2)
        if operacao == '-':
           resultado = int(num1) - int(num2)
        if operacao == '/':
           resultado = int(num1) / int(num2)
        if operacao == '*':
           resultado = int(num1) * int(num2)
        print('O resultado é: ', resultado)
    else:
        print('Número inválido!')
else:
    print('Operação inválida!')