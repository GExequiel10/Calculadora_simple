import helpers.utils as console

from helpers.utils import show_history
from core.operations import add, subtract, multiply, divide


def main():
    console.clear_console()
    while True:
        console.display_menu()
        choice = input('Seleccione una opción (0-5): ')

        try:
            if choice == '0':
                break
            if choice == '1':
                add()
            elif choice == '2':
                subtract()
            elif choice == '3':
                multiply()
            elif choice == '4':
                divide()
            elif choice == '5':
                show_history()
            else:
                print('Opción no válida. Por favor, seleccione una opción del 0 al 5.')
        except Exception as e:
            print(f'Error: {str(e)}. Por favor, intente nuevamente.')


if __name__ == "__main__":
    main()
