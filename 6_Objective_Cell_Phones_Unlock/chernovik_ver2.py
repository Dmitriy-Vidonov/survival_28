# все работы над преобразованием полученного при расчете длины числа - в первой версии черновика
# как оказалось, расчет длины следует делает иначе - как в матрице, свободно передвигаясь к 
# к ближайшим элементам, а не идя строго по линии, как я изначально предполагал

# создаем рабочую матрицу
matrix = []

# задаем переменную длины линии
length = 0

# задаем массив для координат x и y по отдельности
x_coord = []
y_coord = []

codes = [1, 2]

# сформировали матрицу matrix[]
for i in range(3):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(3):
        b.append(0) # заполняем базовые значения массива
    matrix.append(b)

# заполняем матрицу
matrix[0][0] = 6
matrix[0][1] = 1
matrix[0][2] = 9
matrix[1][0] = 5
matrix[1][1] = 2
matrix[1][2] = 8
matrix[2][0] = 4
matrix[2][1] = 3
matrix[2][2] = 7

# выводим матрицу на экран
for x in range(len(matrix)):
    print()
    for y in range(len(matrix[x])):
        print(' ', matrix[x][y], end = ' ')

print()
print()

# по всем элементам массива с кодами разблокировки
for k in range(len(codes)):
    # ищем координаты элементов из codes (входные данные) в matrix (начальная матрица)
    for i in range(3): # 3x3 - размерность матрицы, не меняется по условиям
        for j in range(3):
            if matrix[i][j] == codes[k]:
                x_coord.append(i)
                y_coord.append(j)

# проверка полученных значений
print('x_coord =', x_coord)
print('y_coord =', y_coord)

print()

# *******************URGENT CORRECTIONS*******************
# выяснилось, что в данной задаче следует просто тупым перебором обозначить возможные длины между элементами
# нужен просто большой if для нахождения допустимого соседа или массив допустимых пар переходов

codes = [5, 7]

extra_len = 1.5

print('codes =', codes)

for i in range(len(codes)-1):
    # связи в верхней половине квадрата
    if codes[i] == 1 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 1: length += 1
    elif codes[i] == 1 and codes[i+1] == 5 or codes[i] == 5 and codes[i+1] == 1: length += extra_len
    elif codes[i] == 1 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 1: length += 1
    elif codes[i] == 1 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 1: length += extra_len
    elif codes[i] == 1 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 1: length += 1
    
    # связи в нижней половине квадрата
    elif codes[i] == 3 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 3: length += 1
    elif codes[i] == 3 and codes[i+1] == 5 or codes[i] == 5 and codes[i+1] == 3: length += extra_len
    elif codes[i] == 3 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 3: length += 1
    elif codes[i] == 3 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 3: length += extra_len
    elif codes[i] == 3 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 3: length += 1

    # связи в левой половине квадрата
    elif codes[i] == 5 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 5: length += 1
    elif codes[i] == 5 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 5: length += 1
    elif codes[i] == 5 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 5: length += 1

    # связи в правой половине квадрата
    elif codes[i] == 8 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 8: length += 1
    elif codes[i] == 8 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 8: length += 1
    elif codes[i] == 8 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 8: length += 1
    
    # связи от 2 по диагоналям
    elif codes[i] == 2 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 2: length += extra_len
    elif codes[i] == 2 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 2: length += extra_len
    elif codes[i] == 2 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 2: length += extra_len
    elif codes[i] == 2 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 2: length += extra_len
    
    # непрямые связи для 1
    elif codes[i] == 1 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 1: length += (1 + extra_len)
    elif codes[i] == 1 and codes[i+1] == 3 or codes[i] == 3 and codes[i+1] == 1: length += (1 + 1)
    elif codes[i] == 1 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 1: length += (1 + extra_len)

    # непрямые связи для 3
    elif codes[i] == 3 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 3: length += (1 + extra_len)
    elif codes[i] == 3 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 3: length += (1 + extra_len)

    # непрямые связи для 4
    elif codes[i] == 4 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 4: length += (1 + 1)
    elif codes[i] == 4 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 4: length += (extra_len + extra_len)
    elif codes[i] == 4 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 4: length += (1 + extra_len)
    elif codes[i] == 4 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 4: length += (1 + 1)

    # непрямые связи для 5
    elif codes[i] == 5 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 5: length += (1 + extra_len)
    elif codes[i] == 5 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 5: length += (1 + 1)
    elif codes[i] == 5 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 5: length += (1 + extra_len)

    # непрямые связи для 6
    elif codes[i] == 6 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 6: length += (1 + 1)
    elif codes[i] == 6 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 6: length += (1 + extra_len)
    elif codes[i] == 6 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 6: length += (extra_len + extra_len)
    
    # непрямые связи для 7
    elif codes[i] == 7 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 7: length += (1 + 1)

print('length =', length)