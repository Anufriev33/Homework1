# Задача №30:
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. 
# Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# Решение :


# a1 = int(input("Введите первый элемент: "))
# d = int(input("Введите разность: "))
# n = int(input("Введите количество элементов: "))

# progression = []
# for i in range(n):
#     an = a1 + i * d
#     progression.append(an)

# print("Арифметическая прогрессия:", progression)



# Решение с помощью функции :


def arithmetic_progression(a1, d, n):
    progression = []
    for i in range(n):
        an = a1 + i * d
        progression.append(an)
    return progression

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = arithmetic_progression(a1, d, n)
print("Арифметическая прогрессия:", progression)
