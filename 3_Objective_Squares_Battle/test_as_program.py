# создаем двумерный массив
N = 9 # число строк матрицы
M = 9 # число элементов в строке - число столбцов

def_massiv = [1,1, 9,9] # наш массив, который мы передаем из функуции. чет - в x, нечет - в y

a = []  # задаем рабочий массив

x_massiv_landing_zones = [] # первичный массив для x-координат
y_massiv_landing_zones = [] # первичный массив для y-координат

x_massiv_conquer = [] # вторичный массив для x-координат
y_massiv_conquer = [] # вторичный массив для y-координат

total_sum = 0 # общая сумма элементов массива
dot = 'BOOM'
empty = '----' 

x_coord = 0 # координаты по x, они же N, они же - индекс строки
y_coord = 0 # координаты по y, они же M, они же - индекс столбца
step_length = 1 # длина шага завоевания за 1 день

flag = 0 # флажок для разветвления циклов - запускаем тот или иной цикл в зависимости от флага
days = 0 # задаем счетчик дней

# раскидываем массив на массивы координат x и y
for i in range(len(def_massiv)):
    if i % 2 == 0:
        x_massiv_landing_zones.append(def_massiv[i])
    else:
        y_massiv_landing_zones.append(def_massiv[i])

# сформировали матрицу а[]
for i in range(N):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(M):
        b.append(empty) # заполняем базовые значения массива
    a.append(b)

# проставили точки высадки
for i in range(len(x_massiv_landing_zones)):
    x_coord = x_massiv_landing_zones[i]
    y_coord = y_massiv_landing_zones[i]
    a[x_coord - 1][y_coord - 1] = dot

days += 1

print()
print('Дней прошло:', days)

# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print(' ', a[x][y], end = ' ')
print()

# проверили общую сумму
for i in range(N):
    for j in range(M):
        if a[i][j] == dot:
            total_sum += 1

if total_sum < N * M: 

    # заполнение точки массива исходя из координат
    for i in range(len(x_massiv_landing_zones)):
   
        x_coord = x_massiv_landing_zones[i]
        y_coord = y_massiv_landing_zones[i]
        a[x_coord - 1][y_coord - 1] = dot # ставим точку высадки

        # заполнение по горизонтали
        if y_coord >= (step_length + 1) and a[x_coord - 1][y_coord - step_length - 1] != dot:
            a[x_coord - 1][y_coord - 1 - step_length] = dot
        
            # занесли координаты в промежуточный массив
            x_massiv_conquer.append(x_coord)
            y_massiv_conquer.append(y_coord - step_length)
    
        if y_coord <= (M - step_length) and a[x_coord - 1][y_coord + step_length - 1] != dot:
            a[x_coord - 1][y_coord + step_length - 1] = dot
        
            # занесли координаты в промежуточный массив
            x_massiv_conquer.append(x_coord)
            y_massiv_conquer.append(y_coord + step_length)

        # заполнение по вертикали
        if x_coord >= step_length + 1 and a[x_coord - step_length - 1][y_coord - 1] != dot:
            a[x_coord - 1 - step_length][y_coord - 1] = dot
        
            # занесли координаты в промежуточный массив
            x_massiv_conquer.append(x_coord - step_length)
            y_massiv_conquer.append(y_coord)

        if x_coord <= (N - step_length) and a[x_coord + step_length - 1][y_coord - 1] != dot:
            a[x_coord + step_length - 1][y_coord - 1] = dot

            # занесли координаты в промежуточный массив
            x_massiv_conquer.append(x_coord + step_length)
            y_massiv_conquer.append(y_coord)

    total_sum = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == dot:
                total_sum += 1

    days += 1

    print()
    print('Дней прошло:', days)

    # выводим матрицу на экран
    for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
        print()
        for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
            print(' ', a[x][y], end = ' ')

    print()
    print()
    print('x_massiv_conquer =', x_massiv_conquer)
    print('y_massiv_conquer =', y_massiv_conquer)
    print()

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
                a[x_coord - 1][y_coord - 1] = dot

                # заполнение по горизонтали
                if y_coord >= (step_length + 1) and a[x_coord - 1][y_coord - step_length - 1] != dot:
                    a[x_coord - 1][y_coord - 1 - step_length] = dot
        
                    # занесли координаты в промежуточный массив
                    x_massiv_landing_zones.append(x_coord)
                    y_massiv_landing_zones.append(y_coord - step_length)
    
                if y_coord <= (M - step_length) and a[x_coord - 1][y_coord + step_length - 1] != dot:
                    a[x_coord - 1][y_coord + step_length - 1] = dot
        
                    # занесли координаты в промежуточный массив
                    x_massiv_landing_zones.append(x_coord)
                    y_massiv_landing_zones.append(y_coord + step_length)

                # заполнение по вертикали
                if x_coord >= step_length + 1 and a[x_coord - step_length - 1][y_coord - 1] != dot:
                    a[x_coord - 1 - step_length][y_coord - 1] = dot
        
                    # занесли координаты в промежуточный массив
                    x_massiv_landing_zones.append(x_coord - step_length)
                    y_massiv_landing_zones.append(y_coord)

                if x_coord <= (N - step_length) and a[x_coord + step_length - 1][y_coord - 1] != dot:
                    a[x_coord + step_length - 1][y_coord - 1] = dot

                    # занесли координаты в промежуточный массив
                    x_massiv_landing_zones.append(x_coord + step_length)
                    y_massiv_landing_zones.append(y_coord)

            # обновляем дни
            days += 1
        
            # выводим количество дней
            print('Дней прошло: ', days)

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

            print('total_sum =', total_sum)
            print('flag = ', flag)

    #####################  2 VETKA   ########################

        else:

            # очистим массивы для точек высадки:
            del x_massiv_conquer [:]
            del y_massiv_conquer [:]

            # заполнение точки массива исходя из координат
            for i in range(len(x_massiv_landing_zones)):
                x_coord = x_massiv_landing_zones[i]
                y_coord = y_massiv_landing_zones[i]
                a[x_coord - 1][y_coord - 1] = dot

                # заполнение по горизонтали
                if y_coord >= (step_length + 1) and a[x_coord - 1][y_coord - step_length - 1] != dot:
                    a[x_coord - 1][y_coord - 1 - step_length] = dot
        
                    # занесли координаты в промежуточный массив
                    x_massiv_conquer.append(x_coord)
                    y_massiv_conquer.append(y_coord - step_length)
    
                if y_coord <= (M - step_length) and a[x_coord - 1][y_coord + step_length - 1] != dot:
                    a[x_coord - 1][y_coord + step_length - 1] = dot
        
                    # занесли координаты в промежуточный массив
                    x_massiv_conquer.append(x_coord)
                    y_massiv_conquer.append(y_coord + step_length)

                # заполнение по вертикали
                if x_coord >= step_length + 1 and a[x_coord - step_length - 1][y_coord - 1] != dot:
                    a[x_coord - 1 - step_length][y_coord - 1] = dot
        
                    # занесли координаты в промежуточный массив
                    x_massiv_conquer.append(x_coord - step_length)
                    y_massiv_conquer.append(y_coord)

                if x_coord <= (N - step_length) and a[x_coord + step_length - 1][y_coord - 1] != dot:
                    a[x_coord + step_length - 1][y_coord - 1] = dot

                    # занесли координаты в промежуточный массив
                    x_massiv_conquer.append(x_coord + step_length)
                    y_massiv_conquer.append(y_coord)

            # обновляем дни
            days += 1
        
            # выводим количество дней
            print('Дней прошло: ', days)

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

            print('total_sum =', total_sum)
            print('flag = ', flag)

else:
    # выводим количество дней
    print('Дней прошло: ', days)

    # выводим матрицу на экран
    for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
        print()
        for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
            print(' ', a[x][y], end = ' ')

    print()
    print()
