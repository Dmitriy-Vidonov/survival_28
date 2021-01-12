# создаем двумерный массив
N = 9 # число строк матрицы
M = 9 # число элементов в строке - число столбцов

total_sum = 0 # общая сумма элементов массива
dot = 1 # чем заполняем точки высадки и завоевания. хоть 1, хоть любой символ
empty = '-' # чем заполняем пустые точки массива. по сути можно тоже брать что угодно

a = []  # задаем рабочий массив
for i in range(N):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(M):
        b.append(empty) # заполняем базовые значения массива
    a.append(b)

# задаем первичный массив для x-координат - он же для точек высадки
x_massiv_landing_zones = []
x_massiv_landing_zones = [4]

# задаем первичный массив для y-координат - он же для точек высадки
y_massiv_landing_zones = []
y_massiv_landing_zones = [4]

x_coord = 0 # координаты по x, они же N, они же - индекс строки
y_coord = 0 # координаты по y, они же M, они же - индекс столбца
step_length = 1 # длина шага завоевания за 1 день

x_massiv_conquer = [] # вторичный массив для x-координат
y_massiv_conquer = [] # вторичный массив для y-координат


# заполнение точки массива исходя из координат
for i in range(len(x_massiv_landing_zones)):
    x_coord = x_massiv_landing_zones[i]
    y_coord = y_massiv_landing_zones[i]
    a[x_coord][y_coord] = dot # ставим точку высадки

    # заполнение по горизонтали
    if y_coord >= (0 + step_length) and a[x_coord][y_coord - step_length] != dot:
        a[x_coord][y_coord - step_length] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord)
        y_massiv_conquer.append(y_coord - step_length)
    
    if y_coord <= (M - step_length * 2) and a[x_coord][y_coord + step_length] != dot:
        a[x_coord][y_coord + step_length] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord)
        y_massiv_conquer.append(y_coord + step_length)


    # заполнение по вертикали
    if x_coord >= (0 + step_length) and a[x_coord - step_length][y_coord] != dot:
        a[x_coord - step_length][y_coord] = dot
        
        # занесли координаты в промежуточный массив
        x_massiv_conquer.append(x_coord - step_length)
        y_massiv_conquer.append(y_coord)

    if x_coord <= (N - step_length * 2) and a[x_coord + step_length][y_coord] != dot:
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



flag = 0

while total_sum < N * M:

# ***************************************1 ветка******************************    

    if flag % 2 == 0: # первая ветка:

        # очистим массивы для точек высадки:
        del x_massiv_landing_zones [:]
        del y_massiv_landing_zones [:]

        # заполнение точки массива исходя из координат
        for i in range(len(x_massiv_conquer)):
            x_coord = x_massiv_conquer[i]
            y_coord = y_massiv_conquer[i]
            a[x_coord][y_coord] = dot

            # заполнение по горизонтали
            if y_coord >= (0 + step_length) and a[x_coord][y_coord - step_length] != dot: # здесь в 'and' дополнительно проверяем, не заполнена ли ячейка ранее
                a[x_coord][y_coord - step_length] = dot
        
                # занесли координаты в промежуточный массив
                x_massiv_landing_zones.append(x_coord)
                y_massiv_landing_zones.append(y_coord - step_length)
    
            if y_coord <= (M - step_length * 2) and a[x_coord][y_coord + step_length] != dot:
                a[x_coord][y_coord + step_length] = dot
        
                # занесли координаты в промежуточный массив
                x_massiv_landing_zones.append(x_coord)
                y_massiv_landing_zones.append(y_coord + step_length)

            # заполнение по вертикали
            if x_coord >= (0 + step_length) and a[x_coord - step_length][y_coord] != dot:
                a[x_coord - step_length][y_coord] = dot
        
                # занесли координаты в промежуточный массив
                x_massiv_landing_zones.append(x_coord - step_length)
                y_massiv_landing_zones.append(y_coord)

            if x_coord <= (N - step_length * 2) and a[x_coord + step_length][y_coord]:
                a[x_coord + step_length][y_coord] = dot

                # занесли координаты в промежуточный массив
                x_massiv_landing_zones.append(x_coord + step_length)
                y_massiv_landing_zones.append(y_coord)


        # выводим матрицу на экран
        for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
            print()
            for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
                print(' ', a[x][y], end = ' ')

        # теперь надо вывести спиок новых координат

        print()
        print('x_massiv_landing_zones =', x_massiv_landing_zones)
        print('y_massiv_landing_zones =', y_massiv_landing_zones)
        print()
    
        # обновляем total_sum
        total_sum = 0
        for i in range(N):
            for j in range(M):
                if a[i][j] == dot:
                    total_sum += 1

        # обновляем flag
        flag += 1
    

# ***************************************2 ветка******************************    

    else: # вторая ветка
        # очистим массивы conquer:
        del x_massiv_conquer [:]
        del y_massiv_conquer [:]

        # заполнение точки массива исходя из координат
        for i in range(len(x_massiv_landing_zones)):
            x_coord = x_massiv_landing_zones[i]
            y_coord = y_massiv_landing_zones[i]
            a[x_coord][y_coord] = dot

            # заполнение по горизонтали
            if y_coord >= (0 + step_length) and a[x_coord][y_coord - step_length] != dot:
                a[x_coord][y_coord - step_length] = dot
        
                # занесли координаты в промежуточный массив
                x_massiv_conquer.append(x_coord)
                y_massiv_conquer.append(y_coord - step_length)
    
            if y_coord <= (M - step_length*2) and a[x_coord][y_coord + step_length] != dot:
                a[x_coord][y_coord + step_length] = dot
        
                # занесли координаты в промежуточный массив
                x_massiv_conquer.append(x_coord)
                y_massiv_conquer.append(y_coord + step_length)

            # заполнение по вертикали
            if x_coord >= (0 + step_length) and a[x_coord - step_length][y_coord] != dot:
                a[x_coord - step_length][y_coord] = dot
        
                # занесли координаты в промежуточный массив
                x_massiv_conquer.append(x_coord - step_length)
                y_massiv_conquer.append(y_coord)

            if x_coord <= (N - step_length * 2) and a[x_coord + step_length][y_coord] != dot:
                a[x_coord + step_length][y_coord] = dot

                # занесли координаты в промежуточный массив
                x_massiv_conquer.append(x_coord + step_length)
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

        # обновляем total_sum
        total_sum = 0
        for i in range(N):
            for j in range(M):
                if a[i][j] == dot:
                    total_sum += 1

        # обновляем flag
        flag += 1