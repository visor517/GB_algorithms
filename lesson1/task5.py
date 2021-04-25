# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string

a = input('Введите первую букву a-z: ')
b = input('Введите вторую букву a-z: ')

a_number = string.ascii_lowercase.find(a)
b_number = string.ascii_lowercase.find(b)

if a_number == b_number:
    print(f'Дважды введена буква {a} под номером {a_number + 1}')

else:
    print(f'Введенные буквы находятся в Алфавите на местах {a_number + 1} и {b_number + 1}') 
    between = abs(a_number - b_number) - 1
    print(f'Количество букв между введенными: {between}')