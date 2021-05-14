"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.

3.5. В массиве найти максимальный отрицательный элемент. Вывести на экран его
значение и позицию в массиве.
"""

import random, math, sys

def get_memory(obj):
    result = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                result += get_memory(key)
                result += get_memory(value)
        else:
            for item in obj:
                result += get_memory(item)
    
    return result 

# генерируем массив

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

# решение 1
sum = 0

result = {'pos': -1, 'val': -math.inf}

for index, value in enumerate(array):
    if (value < 0) & (value > result['val']):
        result['pos'] = index
        result['val'] = value

sum += get_memory(result)

if result['pos'] < 0:
    print('В массиве нет отрицательных чисел')
else:
    print(f'Наибольшее отрицательное число {result["val"]} расположено в массиве под индексом {result["pos"]}')

print(f'Вариант 1. Потрачено {sum}')    # 344

"""
Вывод
"""
