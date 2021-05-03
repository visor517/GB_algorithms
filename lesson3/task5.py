"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его
значение и позицию в массиве.

Не используем max() min() sum() sorted()
"""

import random, math

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

result = {'pos': -1, 'val': -math.inf}

#решение

for index, value in enumerate(array):
    if (value < 0) & (value > result['val']):
        result['pos'] = index
        result['val'] = value

if result['pos'] < 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Наибольшее отрицательное число {result["val"]} расположено в массиве под индексом {result["pos"]}')
    