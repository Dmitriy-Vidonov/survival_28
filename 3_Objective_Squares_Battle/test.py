def ConquestCampaign(N: int, M: int, L: int, battalion) -> int:

    a = []  # задаем рабочий массив

    x_massiv_landing_zones = [] # первичный массив для x-координат
    y_massiv_landing_zones = [] # первичный массив для y-координат

    x_massiv_conquer = [] # вторичный массив для x-координат
    y_massiv_conquer = [] # вторичный массив для y-координат

    total_sum = 0 # общая сумма элементов массива
    dot = '+' # чем заполняем точки высадки и завоевания
    empty = '-' # чем заполняем пустые точки массива

    x_coord = 0 # координаты по x
    y_coord = 0 # координаты по y
    step_length = 1 # длина шага завоевания за 1 день

    flag = 0 # флажок для разветвления циклов
    days = 2 # задаем счетчик дней

    # раскидываем массив на массивы координат x и y
    for i in range(len(battalion)):
        if i % 2 == 0:
            x_massiv_landing_zones.append(battalion[i])
        else:
            y_massiv_landing_zones.append(battalion[i])

    for i in range(N):
        b = [] # на каждом шаге делаем очередной вложенный подсписок
        for j in range(M):
            b.append(empty) # заполняем базовые значения массива
        a.append(b)

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

    while total_sum < N * M:  

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
                if y_coord >= (0 + step_length) and a[x_coord][y_coord - step_length] != dot:
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

    return days

massiv = [2,2, 3,4]
print(ConquestCampaign(9,9,2,massiv))
