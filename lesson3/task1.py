"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны
каждому из чисел в диапазоне от 2 до 9.

Не используем max() min() sum() sorted()
"""

result = [0 for _ in range(8)]

number = 2

while number <= 99:

    i = 2
    while i <= 9:
        if number % i == 0:
            result[i-2] += 1

        i +=1

    number +=1

i = 2
while i <= 9:
    print (f'{result[i-2]} чисел кратны {i}')

    i += 1
