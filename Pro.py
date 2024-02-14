import os
import time

def create_file(filename):
    with open(filename, 'w') as f:
        f.write(input("Podaj tekst do zapisania w nowym pliku: "))

def read_file(filename):
    with open(filename, 'r') as f:
        print(f.read())

def list_files():
    print(os.listdir())

def rename_file(old_name, new_name):
    os.rename(old_name, new_name)

def count_chars(filename):
    with open(filename, 'r') as f:
        print("Liczba znaków w pliku:", len(f.read()))

def edit_file(filename):
    with open(filename, 'r+') as f:
        print("Aktualna zawartość pliku:")
        print(f.read())
        f.write(input("Podaj tekst do dodania do pliku: "))

def delete_file(filename):
    os.remove(filename)

while True:

    print(os.getcwd())

    # Menu
    print("1. Utwórz plik")
    print("2. Wyświetl zawartość pliku")
    print("3. Wyświetl pliki w katalogu")
    print("4. Zmień nazwę pliku")
    print("5. Policz znaki w pliku")
    print("6. Edytuj plik")
    print("7. Usuń plik")
    print("8. Reset Menu")
    print("9. Zakończ program")

    choice = input("Wybierz opcję: ")

    if choice == '1':
        filename = input("Podaj nazwę nowego pliku: ")
        create_file(filename)
    elif choice == '2':
        filename = input("Podaj nazwę pliku do odczytu: ")
        read_file(filename)
    elif choice == '3':
        list_files()
    elif choice == '4':
        old_name = input("Podaj obecną nazwę pliku: ")
        new_name = input("Podaj nową nazwę pliku: ")
        rename_file(old_name, new_name)
    elif choice == '5':
        filename = input("Podaj nazwę pliku do policzenia znaków: ")
        count_chars(filename)
    elif choice == '6':
        filename = input("Podaj nazwę pliku do edycji: ")
        edit_file(filename)
    elif choice == '7':
        filename = input("Podaj nazwę pliku do usunięcia: ")
        delete_file(filename)
    elif choice == '9':
        print("Zakończono program.")
        break

    time.sleep(1)
