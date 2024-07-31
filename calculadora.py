
while True:
    print('Escolha uma operação: ')
    print('1. Adição')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Divisão')

    operacao = input('Digite o Número da operação desejada: 1, 2, 3 ou 4:')

    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    if operacao == '1':
        resultado = numero1 + numero2
        print(f'{resultado}Resultado: ')
    elif operacao == '2':
        resultado = numero1 - numero2
        print(f'{resultado}Resultado: ')
    elif operacao == '3':
        resultado = numero1 * numero2
        print(f'{resultado}Resultado: ')
    elif operacao == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f'{resultado}Resultado: ')
        else:
            print('erro: divisão por zero não permitido')
    else:
        print('Operação inválida.')
    continuar =input('Deseja fazer outro cálculo: s/n?')
    if continuar != 's':
        break