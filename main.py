
history = []

def main():
    while True:
        print('Calculadora Simple')
        print('1. Sumar')
        print('2. Restar')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Mostrar Historial')
        print ('0. Salir')
        
        option = input('Seleccione una opción (0-5): ')
        if option in ['0']:
            break
        elif option in ['1', '2', '3', '4']:
            number_1 = float(input('Ingrese el primer operando: '))
            number_2 = float(input('Ingrese el segundo operando: '))
#            resultado = 0

            if option == '0':
                break
            if option == '1':
                resultado = number_1 + number_2
                history.append(f'{number_1} + {number_2} = {resultado}')
                print(f'{number_1} + {number_2} = {resultado}')
            elif option == '2':
                resultado = number_1 - number_2
                history.append(f'{number_1} - {number_2} = {resultado}')
                print(f'{number_1} - {number_2} = {resultado}')
            elif option == '3':
                resultado = number_1 * number_2
                history.append(f'{number_1} * {number_2} = {resultado}')
                print(f'{number_1} * {number_2} = {resultado}')
            elif option == '4':
                resultado = number_1 / number_2
                history.append(f'{number_1} / {number_2} = {resultado}')
                print(f'{number_1} / {number_2} = {resultado}')
        elif option == '5':
            if history:
                print ('>>>Historial de Operaciones:<<<')
                for operation in history:
                    print(operation)
            else:
                print ('Sin operaciones aun...')
            
        else:
            print('Opción no válida. Por favor, seleccione una opción del 1 al 5.')
            
      
if __name__ == "__main__":
    main()
