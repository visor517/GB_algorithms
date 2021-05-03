"""
7. В одномерном массиве целых чисел определить два наименьших элемента. Они
могут быть как равны между собой (оба являться минимальными), так и
различаться.

Не используем max() min() sum() sorted()
"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

#решение

if array[0] <= array[1]:
    most_min_value, min_value = {'pos': 0, 'val': array[0]}, {'pos': 1, 'val': array[1]}
else:
    most_min_value, min_value = {'pos': 1, 'val': array[1]}, {'pos': 0, 'val': array[0]}
    
for index in range(1,len(array)):
    value = array[index]
    if value < min_value['val']:
        if value < most_min_value['val']:
            min_value = most_min_value
            most_min_value = {'pos': index, 'val': value}
        else:
            min_value = {'pos': index, 'val': value}

print(f'Наименьшие числа {most_min_value["val"]} и {min_value["val"]} находятся в массиве под индексами {most_min_value["pos"]} и {min_value["pos"]}')
