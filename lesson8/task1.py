"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

str = input('Введите строку из маленьких латинских букв: ')

# делаем дерево

class Node:
    def __init__ (self, value = None, left = None, right = None, level = 1):
        self.value = value
        self.left = left
        self.right = right
        self.level = level

    def __repr__ (self):
        result = f'[{self.value}]'
        if self.left != None:
            result += f'\n{"  "*self.level}{self.left}'
        if self.right != None:
            result += f'\n{"  "*self.level}{self.right}'
        return result

def get_branches(data, level = 0, isRight = False):
    # level - для формирования отступов при печати
    # isRight - для удаления дублирующих веток по правой стороне

    if len(data) <= 1:
        return Node(data)
    if isRight:
        return Node(data, None, get_branches(data[1:], level + 1, True), level + 1)
    return Node(data, get_branches(data[:-1], level + 1), get_branches(data[1:], level + 1, True), level + 1)

tree = get_branches(str)

print(tree)    # дерево подстрок

# проход по дереву

def harvest(data):
    result = [data.value]
    if data.left:
        result += harvest(data.left)
    if data.right:
        result += harvest(data.right)
    return result

print(f'Подстроки: {harvest(tree)}')    # массив подстрок

# используем hash

def harvest_hash(data, hash_list = []):
    isInHash = False
    value_hash = hashlib.sha1(data.value.encode('utf-8')).hexdigest()
    for item in hash_list:
        if item == value_hash:
            isInHash = True
            break
    
    if not isInHash:
        hash_list.append(value_hash)

    if data.left:
        hash_list = harvest_hash(data.left, hash_list)
    if data.right:
        hash_list = harvest_hash(data.right, hash_list)
    return hash_list

print(f'Ответ: в строке {len(harvest_hash(tree)) - 1} разных подстрок.')
# -1 чтобы не учитывать саму строку
