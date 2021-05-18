"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным
образом. Найдите в массиве медиану. Медианой называется элемент ряда, делящий
его на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки, который
не рассматривался на уроках
"""

import random

M_SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * M_SIZE + 1)]

print(array)
 
# решение

def get_median(data):
    limit = len(data) // 2

    for i in data:
        L = R = 0

        for j in data:
            if j < i:
                L += 1
            if j > i:
                R += 1
        
        if (L <= limit) and (R <= limit):
            return i

print(f'Медиана: {get_median(array)}')
