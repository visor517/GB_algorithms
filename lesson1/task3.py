# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
# https://drive.google.com/file/d/1TrsfcbQ_r2kMn5ZVBMEZbtlQF0rz3chd/view?usp=sharing

ax = float(input('Введите координату Х точки А: '))
ay = float(input('Введите координату У точки А: '))
bx = float(input('Введите координату Х точки Б: '))
by = float(input('Введите координату У точки Б: '))

print('Уравнение прямой проходящей через точки А и Б:')

if ax == bx: 
    print(f'x = {ax}')
else:
    k = (ay - by) / (ax - bx)

    b = ay - k * ax

    print(f'y = {k}x+{b}')