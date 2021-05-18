"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в виде
функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
 
# решение

def my_sort(data):
    j = len(array)

    while j > 1:
        isChanged = False

        for i in range(j - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isChanged = True
        
        if not isChanged:   # досрочный выход из цикла при отсутствии перестановок
            break
        j -= 1

    return data

print(my_sort(array))
