import os

from rich.console import Console

console = Console()

history = []


def add_history(entry):
    history.append(entry)


def show_history():
    print()

    if history:
        console.print('>>>HISTORIAL DE OPERACIONES:<<<', style='bold blue')
        for operation in history:
            print(operation)
    else:
        console.print('Sin operaciones aun...', style='red')


def clear_console():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Linux y macOS
    else:
        os.system('clear')


def display_menu():
    print()
    console.print('CALCULADORA SIMPLE', style='bold green')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Mostrar Historial')
    print('0. Salir')
