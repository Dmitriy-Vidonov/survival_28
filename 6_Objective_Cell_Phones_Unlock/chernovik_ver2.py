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

# задаем массив с кодами разблокировки (входные данные)
codes = [2, 6]

# вывод входного массива на экран
print('codes =', codes)

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

# обрабатываем координаты элементов и считаем длину
for i in range(len(x_coord)-1):
    # горизонталь от центрального элемента
    if x_coord[i+1] == x_coord[i] and y_coord[i+1] - y_coord[i] == 1 or y_coord[i+1] - y_coord[i] == -1:
        length += 1
    
    # вертикаль от центрального элемента
    elif y_coord[i+1] == y_coord[i] and x_coord[i+1] - x_coord[i] == 1 or x_coord[i+1] - x_coord[i] == -1:
        length += 1

    # 1-я диагональ - от левого нижнего края к правому верхнему
    elif x_coord[i+1] - x_coord[i] == -1 or x_coord[i+1] - x_coord[i] == 1 \
        and y_coord[i+1] - y_coord[i] == 1 or y_coord[i+1] - y_coord[i] == 0:
        length += 1.5

    # 2-я диагональ - от левого верхнего края к правому нижнему
    elif x_coord[i+1] - x_coord[i] == 1 or x_coord[i+1] - x_coord[i] == 0 \
        and y_coord[i+1] - y_coord[i] == 1 or y_coord[i+1] - y_coord[i] == 0:
        length += 1.5

# контрольный вывод
print()
print('Length =', length)