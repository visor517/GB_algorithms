"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.

3.1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
каждому из чисел в диапазоне от 2 до 9.
"""

import sys

def get_memory(obj):
    result = sys.getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                result += sys.getsizeof(key)
                result += get_memory(value)
        else:
            for item in obj:
                result += get_memory(item)
    
    return result 

# вариант 1

sum = 0

result = [0 for _ in range(8)]

for number in range(2, 100):

    for i in range(2,10):
        if number % i == 0:
            result[i-2] += 1

sum += get_memory(result)

for i in range(2,10):
    print (f'{result[i-2]} чисел кратны {i}')

print(f'Вариант 1. Потрачено {sum}')    # 344

"""
Другого варианта не придумал к этой задаче.
W10 x64.  Python 3.9.1 64-bit
"""
