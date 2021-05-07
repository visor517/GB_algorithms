"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

import random
import cProfile
from timeit import timeit

def get_array(size):

    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]

    return array

    #решение
def version_1(array):

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

    return array

def version_2(array):

    min_value = min(array)
    max_value = max(array)

    min_index = array.index(min_value)
    max_index = array.index(max_value)

    array[min_index] = max_value
    array[max_index] = min_value

    return array

#анализ
for size in [10, 100, 1000, 10000, 100000]:

    array = get_array(size)

    print('v1:', timeit('version_1(array)', number = 1000, globals = globals()))
    #0.0038262999999999978
    #0.0424673
    #0.302829
    #3.1350311
    #29.696589799999998

    print('v2:', timeit('version_2(array)', number = 1000, globals = globals()))
    #0.0015420999999999976
    #0.006171899999999994
    #0.02730680000000002
    #0.26188140000000004
    #2.6784766000000033

#cProfile.run('version_1(array)')
#cProfile.run('version_2(array)')

"""
Вывод:
Оба решения имеют линейную сложно.
Вариант с использованием готовых методов max, min, index работает на порядок быстрее.
Предположу, что из-за отсутстви дополнительных операций для организации цикла i, len(array)
и хранения промежуточных значений min_value и max_value.

"""

