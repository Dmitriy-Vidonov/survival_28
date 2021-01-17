def ConquestCampaign(N: int, M: int, L: int, battalion) -> int:

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
    for i in range(len(battalion)):
        if i % 2 == 0:
            x_massiv_landing_zones.append(battalion[i])
        else:
            y_massiv_landing_zones.append(battalion[i])

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

        while total_sum < N * M: 

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
    
                # обновляем total_sum
                total_sum = 0
                for i in range(N):
                    for j in range(M):
                        if a[i][j] == dot:
                            total_sum += 1

                # обновляем flag
                flag += 1

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
    
                # обновляем total_sum
                total_sum = 0
                for i in range(N):
                    for j in range(M):
                        if a[i][j] == dot:
                            total_sum += 1

                # обновляем flag
                flag += 1

    else:
        return days

    return days

massiv = [1,1, 9,9]
print(ConquestCampaign(9,9,2,massiv))