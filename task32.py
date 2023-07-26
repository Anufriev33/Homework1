# Задача №32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного  максимума)


# Решение c приминением функции :


# def find_indexes(arr, min_val, max_val):
#     indexes = []
#     for i in range(len(arr)):
#         if  min_val<= arr[i] <= max_val:
#             indexes.append(i)
#     return indexes

# arr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_val =6
# max_val = 10

# result = find_indexes(arr, min_val, max_val)
# print(result)


# Решение с применением List_Comprehension c функцией enumerate :


# lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_val = 6
# max_val = 10

# indexes = [i for i, num in enumerate(lst) if num >= min_val and num <= max_val]
# print(indexes)


# Решение с вводом минимального  значения и максимального значения :


# array = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_val = int(input("Введите минимальное значение: "))
# max_val = int(input("Введите максимальное значение: "))

# indices = []
# for i in range(len(array)):
#     if min_val <= array[i] <= max_val:
#         indices.append(i)

# print("Индексы элементов, принадлежащих заданному диапазону:", indices)
