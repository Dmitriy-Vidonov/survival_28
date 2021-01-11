# создаем двумерный массив
N = 3 # число строк матрицы
M = 4 # число элементов в строке - число столбцов

a = []
for i in range(N):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(M):
        b.append(0)
    a.append(b)

# вывод массива массивов в чистом виде:
print(a)

print()
print('*************')
print('len(a) =', len(a))

# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')

print()
print()
print('x =', x)
print('len(a[x]) =', len(a[x]))

# задаем массив координат по X
x_massiv = []
x_massiv = [2,0,1]

# задаем массив координат по y
y_massiv = []
y_massiv = [3,0,1]

x_coord = 0 # координаты по x, они же N, они же - индекс строки
y_coord = 0 # координаты по y, они же M, они же - индекс столбца
step_length = 1 # длина шага завоевания за 1 день

# заполнение точки массива исходя из координат
for i in range(len(x_massiv)):
    x_coord = x_massiv[i]
    y_coord = y_massiv[i]
    a[x_coord][y_coord] = 1

    # заполнение по горизонтали
    if y_coord >= (0 + 1):
        a[x_coord][y_coord - step_length] = 1
    
    if y_coord <= (M - 2):
        a[x_coord][y_coord + step_length] = 1

    # заполнение по вертикали
    if x_coord >= (0 + 1):
        a[x_coord - step_length][y_coord] = 1

    if x_coord <= (N - 2):
        a[x_coord + step_length][y_coord] = 1
    
        

# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')