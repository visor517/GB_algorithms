"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
отсортированный массивы.
"""

import random

SIZE = 10
MAX_ITEM = 50
array = [random.random() * MAX_ITEM for _ in range(SIZE)]

print(array)
 
# решение

def merge_sort(data):
    if len(data) > 1:
        L, R = merge_sort(data[:len(data) // 2]), merge_sort(data[len(data) // 2:])

        i = 0
        j = 0
        result = []

        while len(result) < len(L) + len(R):
            if i == len(L):
                result += R[j:]
                break
            elif j == len(R):
                result += L[i:]
                break
            else:

                if L[i] < R[j]:
                    result.append(L[i])
                    i += 1
                else:
                    result.append(R[j])
                    j += 1
        
        return result
    return data

print(merge_sort(array))
