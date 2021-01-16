# создаем двумерный массив
N = 9 # число строк матрицы
M = 9 # число элементов в строке - число столбцов

def_massiv = [2,2, 3,4] # наш массив, который мы передаем из функуции. чет - в x, нечет - в y

x_massiv_landing_zones = [] # первичный массив для x-координат
y_massiv_landing_zones = [] # первичный массив для y-координат

x_massiv_conquer = [] # вторичный массив для x-координат
y_massiv_conquer = [] # вторичный массив для y-координат

total_sum = 0 # общая сумма элементов массива
dot = 'BOOM' # чем заполняем точки высадки и завоевания. хоть 1, хоть любой символ
empty = '----' # чем заполняем пустые точки массива. по сути можно тоже брать что угодно

x_coord = 0 # координаты по x, они же N, они же - индекс строки
y_coord = 0 # координаты по y, они же M, они же - индекс столбца
step_length = 1 # длина шага завоевания за 1 день

flag = 0 # флажок для разветвления циклов - запускаем тот или иной цикл в зависимости от флага
days = 2 # задаем счетчик дней

# раскидываем массив на массивы координат x и y
for i in range(len(def_massiv)):
    if i % 2 == 0:
        x_massiv_landing_zones.append(def_massiv[i])
    else:
        y_massiv_landing_zones.append(def_massiv[i])

a = []  # задаем рабочий массив
for i in range(N):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(M):
        b.append(empty) # заполняем базовые значения массива
    a.append(b)

# заполнение точки массива исходя из координат
for i in range(len(x_massiv_landing_zones)):
    x_coord = x_massiv_landing_zones[i]
    y_coord = y_massiv_landing_zones[i]
    a[x_coord-1][y_coord-1] = dot # ставим точку высадки

    # заполнение по горизонтали
    if y_coord - 1 >= (0 + step_length - 1) and a[x_coord - 1][y_coord - 1 - step_length] != dot:
        a[x_coord - 1][y_coord - step_length - 1] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord)
        y_massiv_conquer.append(y_coord - step_length)
    
    if y_coord - 1 <= (M - step_length * 2 - 1) and a[x_coord - 1][y_coord + step_length - 1] != dot:
        a[x_coord - 1][y_coord + step_length - 1] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord)
        y_massiv_conquer.append(y_coord + step_length)

    # заполнение по вертикали
    if x_coord - 1 >= (0 + step_length - 1) and a[x_coord - step_length - 1][y_coord - 1] != dot:
        a[x_coord - step_length - 1][y_coord - 1] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord - step_length)
        y_massiv_conquer.append(y_coord)

    if x_coord - 1 <= (N - step_length * 2 - 1) and a[x_coord + step_length - 1][y_coord - 1] != dot:
        a[x_coord + step_length - 1][y_coord - 1] = dot

        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord + step_length)
        y_massiv_conquer.append(y_coord)
    
# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')

print()
print('Координаты точек после завоевания с точки высадки (конец 2-ого дня):')
print('x_massiv_conquer =', x_massiv_conquer)
print('y_massiv_conquer =', y_massiv_conquer)
print()