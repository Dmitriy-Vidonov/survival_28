# создаем двумерный массив
N = 7 # число строк матрицы
M = 9 # число элементов в строке - число столбцов

a = []
for i in range(N):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(M):
        b.append('-') # заполняем базовые значения массива
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
x_massiv = [1, 2]

# задаем массив координат по y
y_massiv = []
y_massiv = [1, 3]

x_coord = 0 # координаты по x, они же N, они же - индекс строки
y_coord = 0 # координаты по y, они же M, они же - индекс столбца
step_length = 1 # длина шага завоевания за 1 день

x_massiv_conquer = []
y_massiv_conquer = []

dot = '1' # чем заполняем точки высадки и завоевания. хоть 1, хоть любой символ

# заполнение точки массива исходя из координат
for i in range(len(x_massiv)):
    x_coord = x_massiv[i]
    y_coord = y_massiv[i]
    a[x_coord][y_coord] = dot

    # заполнение по горизонтали
    if y_coord >= (0 + step_length):
        a[x_coord][y_coord - step_length] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord)
        y_massiv_conquer.append(y_coord - step_length)
    
    if y_coord <= (M - step_length*2):
        a[x_coord][y_coord + step_length] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord)
        y_massiv_conquer.append(y_coord + step_length)


    # заполнение по вертикали
    if x_coord >= (0 + step_length):
        a[x_coord - step_length][y_coord] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord - step_length)
        y_massiv_conquer.append(y_coord)

    if x_coord <= (N - step_length*2):
        a[x_coord + step_length][y_coord] = dot

        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord + step_length)
        y_massiv_conquer.append(y_coord)
    
        

# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')

print()
print('Координаты точек после завоевания с точки высадки:')
print('x_massiv_conquer =', x_massiv_conquer)
print('y_massiv_conquer =', y_massiv_conquer)
print()

