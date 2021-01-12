# создаем двумерный массив
N = 9 # число строк матрицы
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

# задаем массив координат по X - для точек высадки
x_massiv_landing_zones = []
x_massiv_landing_zones = [4]

# задаем массив координат по y - для точек высадки
y_massiv_landing_zones = []
y_massiv_landing_zones = [4]

x_coord = 0 # координаты по x, они же N, они же - индекс строки
y_coord = 0 # координаты по y, они же M, они же - индекс столбца
step_length = 1 # длина шага завоевания за 1 день

x_massiv_conquer = [] # массив для точек после 2-ого дня завоевания (1-й - это точка высадки)
y_massiv_conquer = [] # массив для точек после 2-ого дня завоевания (1-й - это точка высадки)

dot = 1 # чем заполняем точки высадки и завоевания. хоть 1, хоть любой символ

# заполнение точки массива исходя из координат
for i in range(len(x_massiv_landing_zones)):
    x_coord = x_massiv_landing_zones[i]
    y_coord = y_massiv_landing_zones[i]
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
print('Координаты точек после завоевания с точки высадки (конец 2-ого дня):')
print('x_massiv_conquer =', x_massiv_conquer)
print('y_massiv_conquer =', y_massiv_conquer)
print()

# запустим тот же цикл с новыми координатами из massiv_conquer
print('Запускаем цикл с новыми координатами. 3-й день завоевания')


# очистим массивы для точек высадки:
del x_massiv_landing_zones [:]
del y_massiv_landing_zones [:]


# заполнение точки массива исходя из координат
for i in range(len(x_massiv_conquer)):
    x_coord = x_massiv_conquer[i]
    y_coord = y_massiv_conquer[i]
    a[x_coord][y_coord] = dot

    # заполнение по горизонтали
    if y_coord >= (0 + step_length):
        a[x_coord][y_coord - step_length] = dot
        
        # занесли координаты в промежуточный массив
        if x_coord != dot:
            x_massiv_landing_zones.append(x_coord)
        if y_coord - step_length != dot:
            y_massiv_landing_zones.append(y_coord - step_length)
    
    if y_coord <= (M - step_length*2):
        a[x_coord][y_coord + step_length] = dot
        
        # занесли координаты в промежуточный массив
        if x_coord != dot:
            x_massiv_landing_zones.append(x_coord)
        if y_coord + step_length != dot:
            y_massiv_landing_zones.append(y_coord + step_length)


    # заполнение по вертикали
    if x_coord >= (0 + step_length):
        a[x_coord - step_length][y_coord] = dot
        
        # занесли координаты в промежуточный массив
        if x_coord - step_length != dot:
            x_massiv_landing_zones.append(x_coord - step_length)
        if y_coord != dot:
            y_massiv_landing_zones.append(y_coord)

    if x_coord <= (N - step_length*2):
        a[x_coord + step_length][y_coord] = dot

        # занесли координаты в промежуточный массив
        if x_coord + step_length != dot:
            x_massiv_landing_zones.append(x_coord + step_length)
        if y_coord != dot:
            y_massiv_landing_zones.append(y_coord)


# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')


# теперь надо вывести спиок новых координат

print()
print('Координаты точек после завоевания (здесь их должно быть уже 8):') # 1 день - точка высадки, 2 день - по клетке от высадок, 3 день - еще по клетке
print('Здесь выводим содержимое уже массивов, которые были раньше для зон высадки:')
print('x_massiv_landing_zones =', x_massiv_landing_zones)
print('y_massiv_landing_zones =', y_massiv_landing_zones)
print()


# заполним матрицу исходя из того, что у нас вышло с массивов landing_zones
# поменяем местами массивы по сути, conquer обнулим, запишем в них новые данные
# а идти будем по циклу с landing_zones

# очистим массивы conquer:
del x_massiv_conquer [:]
del y_massiv_conquer [:]


# заполнение точки массива исходя из координат
for i in range(len(x_massiv_landing_zones)):
    x_coord = x_massiv_landing_zones[i]
    y_coord = y_massiv_landing_zones[i]
    a[x_coord][y_coord] = dot

    # заполнение по горизонтали
    if y_coord >= (0 + step_length):
        a[x_coord][y_coord - step_length] = dot
        
        # занесли координаты в промежуточный массив
        if x_coord != dot:
            x_massiv_conquer.append(x_coord)
        if y_coord - step_length != dot:
            y_massiv_conquer.append(y_coord - step_length)
    
    if y_coord <= (M - step_length*2):
        a[x_coord][y_coord + step_length] = dot
        
        # занесли координаты в промежуточный массив
        if x_coord != dot:
            x_massiv_conquer.append(x_coord)
        if y_coord + step_length != dot:
            y_massiv_conquer.append(y_coord + step_length)


    # заполнение по вертикали
    if x_coord >= (0 + step_length):
        a[x_coord - step_length][y_coord] = dot
        
        # занесли координаты в промежуточный массив
        if x_coord - step_length != dot:
            x_massiv_conquer.append(x_coord - step_length)
        if y_coord != dot:
            y_massiv_conquer.append(y_coord)

    if x_coord <= (N - step_length*2):
        a[x_coord + step_length][y_coord] = dot

        # занесли координаты в промежуточный массив
        if x_coord + step_length != dot:
            x_massiv_conquer.append(x_coord + step_length)
        if y_coord != dot:
            y_massiv_conquer.append(y_coord)


# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')

# теперь надо вывести спиок новых координат

print()
print('x_massiv_conquer =', x_massiv_conquer)
print('y_massiv_conquer =', y_massiv_conquer)
print()