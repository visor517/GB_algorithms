"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме
цифр. Вывести на экран это число и сумму его цифр.
"""

print('Вводите последовательность чисел по одному. Для завершения последовательности наберите q')

max = 0

while True:
    i = input('Введит число: ').lower()
    if i == 'q':
        break
    else:
        if int(i) > max:
            max = int(i)

print(f'Наибольшее введенное число {max}')

max = str(max)
i = 0
sum = 0

while i < len(max):
    sum += int(max[i])

    i += 1

print(f'Сумма цифр максимльного числа: {sum}')