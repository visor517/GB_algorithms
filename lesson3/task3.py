"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

Не используем max() min() sum() sorted()
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

#решение

min_value = {'pos': 0, 'val': array[0]}
max_value = {'pos': 0, 'val': array[0]}

i = 1
while i < len(array) - 1:
    if array[i] < min_value['val']:
        min_value['pos'] = i
        min_value['val'] = array[i]

    if array[i] > max_value['val']:
        max_value['pos'] = i
        max_value['val'] = array[i]

    i += 1

array[min_value['pos']] = max_value['val']
array[max_value['pos']] = min_value['val']

print(array)
