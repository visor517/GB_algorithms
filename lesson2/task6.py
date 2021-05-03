"""
6. В программе генерируется случайное целое число от 0 до 100. Пользователь
должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки
должно сообщаться больше или меньше введенное пользователем число, чем то, что
загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
"""

import random

n = random.randint(0,100)

attempts = 10

while attempts > 0:
    attempts -= 1

    i = int(input('Введите число: '))

    if i > n:
        print('Ваше число больше n')
    elif i < n:
        print('Ваше число меньше n')    
    else:
        print('Вы угадали!')
        break

    if attempts == 0:
        print(f'Было загадано число {n}')