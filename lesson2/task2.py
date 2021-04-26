# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/1IgfwNTV6w1UxsVHWMIOlMyW1eOpXezgW/view?usp=sharing

string = input('Введите натуральное число: ')

even = 0
not_even = 0
i = 0

while i < len(string):
    if int(string[i]) % 2 == 0:
        even += 1
    else:
        not_even += 1
        
    i += 1

print(f'Нечетных цифр: {not_even}. Четных цифр {even}.')