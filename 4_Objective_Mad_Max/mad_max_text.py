tele = [7,6,4,2,1,5,3]
N = len(tele) # 7

centre_coord = 0

max_el = tele[0]
min_el = tele[0]
max_el_coord = 0
min_el_coord = 0

# выводим начальный массив на экран
print(tele)

# расчитали макс. элемент массива
for i in range (len(tele)):
    if tele[i] >= max_el:
        max_el = tele[i]

print('max_el =', max_el)

# расчитали минимальный элемент массива
for i in range (len(tele)):
    if tele[i] <= min_el:
        min_el = tele[i]

print('min_el =', min_el)

# получаем координаты центрального элемента:
centre_coord = int((N - 1) / 2)

print('centre_coord =', centre_coord)

# получаем координаты максимального элемента
for i in range(len(tele)):
    if tele[i] == max_el:
        max_el_coord = i

print('max_el_coord =', max_el_coord)

# получаем координаты минимального элемента
for i in range(len(tele)):
    if tele[i] == min_el:
        min_el_coord = i

print('min_el_coord =', min_el_coord)


# меняем местами максимальный и центральный элементы массива
tele[centre_coord], tele[max_el_coord] = tele[max_el_coord], tele[centre_coord]

# меняем местами минимальный и первый элементы массива
tele[0], tele[min_el_coord] = tele[min_el_coord], tele[0]

# выводим массив с макс. элементом в центре
print(tele)


# сортировать надо так, чтобы пробегать по всему массиву, но минуя максимальный элемент
# сортировка массива до центра по возрастанию
j = 0
sort_left = tele[j]

for i in range(0, len(tele)):
    for j in range(0, centre_coord):
        if tele[i] <= tele[j]:
            tele[i], tele[j] = tele[j], tele[i]

print('tele =', tele)

# сортирвока массива от центра по убыванию
j = centre_coord + 1 
sort_right = tele[j]

for i in range(len(tele)):
    for j in range(centre_coord + 1, len(tele)):
        if tele[i] >= tele[j] and tele[i] != max_el:
            tele[i], tele[j] = tele[j], tele[i]

print('tele =', tele)

