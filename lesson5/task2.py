"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При
этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’,
‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение -
[‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

converter =['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

a = deque(input('Введите первое число: ').upper())
b = deque(input('Введите второе число: ').upper())

# сложение
def alignment (a, b):
    while len(a) > len(b):
        b.appendleft('0')
    while len(b) > len(a):
        a.appendleft('0')
    
    return (a, b)

def summation (a, b):
    result = deque()
    sixteen = 0

    (a, b) = alignment(a, b)

    while len(a) > 0:
        number = converter.index(a.pop()) + converter.index(b.pop()) + sixteen

        if number > 15:
            number -= 16
            sixteen = 1
        else:
            sixteen = 0

        result.appendleft(converter[number])

    if sixteen == 1:
        result.appendleft('1')

    return result

a1 = a.copy()
b1 = b.copy()

print(f'Сумма: {summation(a1, b1)}')

# умножение

result2 = deque()

a2 = a.copy()
b2 = b.copy()

result = deque()

for j in range(len(b2)):
    
    for i in range(converter.index(b2.pop())):

        result = summation(result, a2.copy())

    a2.append('0')

print(f'Произведение: {result}')
