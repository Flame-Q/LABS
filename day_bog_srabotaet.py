# что-то должно хранить фамилию должность и зп, сделать добавление удаление и изменение, итог в файл вывести
my_dict = {}

def save_to_file():
    with open('baza.txt', 'w', encoding='utf-8') as file:
        for fam, (dol, zp) in my_dict.items():
            file.write(f"{fam},{dol},{zp}")
    print("Данные сохранены в файл baza.txt")

def add_employee():
    fam = input("Введите фамилию: ")
    dol = input("Введите должность: ")
    zp = int(input("Введите зарплату: "))
    my_dict[fam] = (dol, zp)
    print(f"Сотрудник {fam} добавлен")
    save_to_file()

def remove_employee():
    fam = input("Введите фамилию для удаления: ")
    if fam in my_dict:
        del my_dict[fam]
        print(f"Сотрудник {fam} удален")
        save_to_file()
    else:
        print("Сотрудник не найден")

def change_surname():
    fam1 = input("Введите фамилию, которую меняете: ")
    if fam1 in my_dict:
        fam2 = input("Введите новую фамилию: ")
        dol, zp = my_dict[fam1]
        del my_dict[fam1]
        my_dict[fam2] = (dol, zp)
        print(f"Фамилия изменена с {fam1} на {fam2}")
        save_to_file()
    else:
        print("Сотрудник не найден")

def change_position():
    fam = input("Введите фамилию сотрудника: ")
    if fam in my_dict:
        dol, zp = my_dict[fam]
        new_dol = input("Введите новую должность: ")
        my_dict[fam] = (new_dol, zp)
        print(f"Должность сотрудника {fam} изменена на {new_dol}")
        save_to_file()
    else:
        print("Сотрудник не найден")

def change_salary():
    fam = input("Введите фамилию сотрудника: ")
    if fam in my_dict:
        dol, zp = my_dict[fam]
        new_zp = int(input("Введите новую зарплату: "))
        my_dict[fam] = (dol, new_zp)
        print(f"Зарплата сотрудника {fam} изменена на {new_zp}")
        save_to_file()
    else:
        print("Сотрудник не найден")

def show_all():
    if not my_dict:
        print("База данных пуста")
        return
    
    print("--- Список сотрудников ---")
    for fam, (dol, zp) in my_dict.items():
        print(f"Фамилия: {fam}, Должность: {dol}, Зарплата: {zp}")
    print("--------------------------")

while True:
    print("-----Меню------")
    print("1. Добавление сотрудника")
    print("2. Удаление сотрудника")
    print("3. Заменить фамилию")
    print("4. Заменить должность")
    print("5. Заменить зарплату")
    print("6. Показать всех сотрудников")
    print("7. Выход")
    
    a = int(input("Выберите действие: "))
        
    if a == 1:
        add_employee()
    elif a == 2:
        remove_employee()
    elif a == 3:
        change_surname()
    elif a == 4:
            change_position()
    elif a == 5:
            change_salary()
    elif a == 6:
            show_all()
    elif a == 7:
            print("Выход из программы")
            break
    else:
        print("Неверный выбор. Попробуйте снова.")
    