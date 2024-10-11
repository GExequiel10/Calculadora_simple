from helpers.utils import history


def add():
    number_1 = float(input('Ingrese el primer operando: '))
    number_2 = float(input('Ingrese el segundo operando: '))
    resultado = number_1 + number_2
    history.append(f'{number_1} + {number_2} = {resultado}')
    print(f'{number_1} + {number_2} = {resultado}')


def subtract():
    number_1 = float(input('Ingrese el primer operando: '))
    number_2 = float(input('Ingrese el segundo operando: '))
    resultado = number_1 - number_2
    history.append(f'{number_1} - {number_2} = {resultado}')
    print(f'{number_1} - {number_2} = {resultado}')


def multiply():
    number_1 = float(input('Ingrese el primer operando: '))
    number_2 = float(input('Ingrese el segundo operando: '))
    resultado = number_1 * number_2
    history.append(f'{number_1} * {number_2} = {resultado}')
    print(f'{number_1} * {number_2} = {resultado}')


def divide():
    number_1 = float(input('Ingrese el primer operando: '))
    number_2 = float(input('Ingrese el segundo operando: '))
    resultado = number_1 / number_2
    history.append(f'{number_1} / {number_2} = {resultado}')
    print(f'{number_1} / {number_2} = {resultado}')
