def MadMax(N: int, Tele):
    
    centre_coord = 0
    max_el = 0
    max_el_coord = 0
    min_el = 0
    min_el_coord = 0
    j = 0
    sort = 0

    # расчитали макс. элемент массива
    for i in range (len(Tele)):
        if Tele[i] >= max_el:
            max_el = Tele[i]

    # получаем координаты центрального элемента:
    centre_coord = int((N - 1) / 2)

    # получаем координаты максимального элемента
    for i in range(len(Tele)):
        if Tele[i] == max_el:
            max_el_coord = i

    # меняем местами максимальный и центральный элементы массива
    Tele[centre_coord], Tele[max_el_coord] = Tele[max_el_coord], Tele[centre_coord]

    # расчитали минимальный элемент массива
    for i in range (len(Tele)):
        if Tele[i] <= min_el:
            min_el = Tele[i]

    # получаем координаты минимального элемента
    for i in range(len(Tele)):
        if Tele[i] == min_el:
            min_el_coord = i

    # меняем местами минимальный и первый элементы массива
    Tele[0], Tele[min_el_coord] = Tele[min_el_coord], Tele[0]

    # сортировка массива до центра по возрастанию
    sort = Tele[j]
    
    for i in range(0, len(Tele)):
        for j in range(0, centre_coord):
            if Tele[i] <= Tele[j]:
                Tele[i], Tele[j] = Tele[j], Tele[i]

    # сортировка массива от центра по убыванию
    if N >= 3:
        j = centre_coord + 1  
    
    else:
        j = centre_coord
    
    sort = Tele[j]

    for i in range(len(Tele)):
        for j in range(centre_coord + 1, len(Tele)):
            if Tele[i] >= Tele[j] and Tele[i] != max_el:
                Tele[i], Tele[j] = Tele[j], Tele[i]

    return Tele