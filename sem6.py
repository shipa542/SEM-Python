# Дана последовательность чисел. Получить список
# уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


# my_list = [5, 3, 2, 5, 10, 15, 10, 8, 3, 8]

# def get_unic(my_list):
#     unic = []
#     for i in range(len(my_list)):
#         if my_list[i] not in my_list[i+1::] and my_list[i] not in my_list[:i-1:]:
#             unic.append(my_list[i])
#     return unic

# print(get_unic(my_list))









# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print("Число должно быть integer ")
#     return number


# def mult(n):
#     if n == 1:
#         return 1
#     else:
#         return n * mult(n - 1)


# num = InputNumbers("Введите число: ")

# list = []
# for e in range(1, num + 1):
#     list.append(mult(e))

# print(f"Произведения чисел от 1 до {num}:  {list}")


# Другое решение задачи


# def Factorial(numb):
#     if numb ==1:
#         return 1
#     else:
#         return numb * Factorial(numb - 1)


# print(*list(map(Factorial, [i for i in range(1, int(input('Введите число: ')) + 1)])))






# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# исходный вариант решения


# list = [2, 3, 5, 9, 3, 8, 5, 2]
# i = 1
# sum = 0
# print("-> на нечётных позициях элементы")
# while i <= len(list):
#     print(list[i])
#     sum = sum + list[i]
#     i += 2
# print("сумма элементов на нечетных позициях: ", sum)



# пример с использованием map

# print("Введите числа через пробел")
# lst = list(map(int, input().split()))
# i = 1
# sum = 0
# print("-> на нечётных позициях элементы")
# while i <= len(lst):
#     print(lst[i])
#     sum = sum + lst[i]
#     i += 2
# print("сумма элементов на нечетных позициях: ", sum)



# добавил enumerate, filter и list comprehension


# lst = [2, 3, 5, 9, 3, 8, 5, 2]
# lst_enum = list(enumerate(lst))

# def odd(x):
#     return x[0] % 2

# lst_odd = list(filter(odd, lst_enum))
# print("сумма элементов на нечетных позициях: ", sum([x[1] for x in lst_odd]))



# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


# исходный вариант решения (уже с list comprehension):

# first_list = [21, 3, 54, 92, 35, 80, 54, 21, 8, 19, 8]
# print("Исходный список: ", first_list)
# new_list = []
# [new_list.append(i) for i in first_list if i not in new_list]
# print("Неповторяющиеся элементы исходного списка: ", new_list)


# добавил map

# first_list = list(map(int, input("Введите числа через пробел:\n").split()))
# print("Исходный список: ", first_list)
# new_list = []
# [new_list.append(i) for i in first_list if i not in new_list]
# print("Неповторяющиеся элементы исходного списка: ", new_list)






# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# txt = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {txt}")
# find_txt = "абв"
# lst = [i for i in txt.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')



# Другое решение задачи


# inp = list(map(str, input("Введите текст: ").split()))
# sample = input("Введите удаляемый текст: ")
# print(list(filter(lambda x: x != sample,inp)))