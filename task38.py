#Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


#Решение:


import os

filename = "tell.txt"

def load_tel():
    if os.path.isfile(filename):
        with open(filename, encoding="UTF-8") as f:
            r = f.readlines()
            s = []
            for line in r:
                s.append(line.split())
        return s
    s = []
    return s

def input_tel(s):
    first_name = input("Введите имя: ")
    patronimic = input("Введите отчество: ")
    last_name = input("Введите фамилию: ")
    tel = input("Введите телефон: ")
    with open(filename, "a", encoding="UTF-8") as f:
        f.write(f"{last_name} {first_name} {patronimic} {tel} \n")
    s.append([last_name, first_name, patronimic, tel])
    return s

def search_tel(s, object):
    for line in s:
        if object in line or object.capitalize() in line:
            return " ".join(line)
    return "Записи не найдено"

def show_tell(s):
    for line in s:
        print(" ".join(line))

def edit_tel(s):
    last_name = input("Введите фамилию человека, данные которого хотите изменить: ")
    for line in s:
        if last_name in line:
            print("Найдены следующие данные:", line)
            action = input("1 - Изменить фамилию \n2 - Изменить имя \n3 - Изменить отчество \n4 - Изменить телефон \n5 - Вернуться в основное меню: ")
            if action == "1":
                new_last_name = input("Введите новую фамилию: ")
                line[0] = new_last_name
            elif action == "2":
                new_first_name = input("Введите новое имя: ")
                line[1] = new_first_name
            elif action == "3":
                new_patronimic = input("Введите новое отчество: ")
                line[2] = new_patronimic
            elif action == "4":
                new_tel = input("Введите новый телефон: ")
                line[3] = new_tel
            elif action == "5":
                return s
            else:
                print("Неправильный ввод!")
            return s
    print("Записи не найдены")
    return s


def delete_tel(s):
    last_name = input("Введите фамилию человека, данные которого хотите удалить: ")
    for line in s:
        if last_name in line:
            print("Найдены следующие данные:", line)
            action = input("Введите последнюю строку данных, которую хотите удалить: ")
            s.remove(action)
            print("Данные успешно удалены.")
            break
    else:
        print("Данные не найдены.")
    return s

if __name__ == "__main__":
    s = load_tel()
    while True:
        action = input("1 - Добавить данные \n2 - Искать данные \n3 - Посмотреть данные \n4 - Изменить данные\n5 - Удалить данные \n6 - Выход \n")
        if action == "1":
            s = input_tel(s)
        elif action == "2":
            search_name = input("Введите ФИО или номер :")
            print(search_tel(s, search_name))
        elif action == "3":
            show_tell(s)
        elif action == "4":
            s = edit_tel(s) 
            print(edit_tel(s))
            break
        elif action == "5":
            print(delete_tel(s)) 
        elif action == "6":
            print("Досвидания!")     
            break
        else:
            print("Данные не найдены!!!")
            break