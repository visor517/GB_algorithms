"""
8. Посчитать, сколько раз встречается определенная цифра в введенной
последовательности чисел. Количество вводимых чисел и цифра, которую необходимо
посчитать, задаются вводом с клавиатуры.

Не использовать списки
"""

number = int(input('Введите цифру 0..9 которую нужно посчитать: '))

quantity = int(input('Введите количество вводимых чисел: '))

count = 0

for i in range(1, quantity + 1):
    item = int(input(f'Введите число {i}: '))

    while item > 0:
        if item % 10 == number:
            count += 1

        item //= 10 

print(f'Цифра {number} использовалась {count} раз')