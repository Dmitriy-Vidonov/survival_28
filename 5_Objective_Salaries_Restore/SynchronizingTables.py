def SynchronizingTables(N: int, ids: int, salary: int) -> int:

    ids_used_els = []
    ids_used_coords = []
    ids_min_el = 0
    ids_min_el_coord = 0
    sorted_sal = []

    sals = dict()

    for k in range(len(ids)):
    
        # находим минимальный элемент в ids
        for x in range(len(ids)):
            if ids[x] in ids_used_els:
                continue
            else:
                break

        ids_min_el = ids[x]

        for i in range(len(ids)):
            if ids[i] <= ids_min_el and ids[i] not in ids_used_els:
                ids_min_el = ids[i]

        ids_used_els.append(ids_min_el)

        # находим координаты минимального элемента в ids
        for j in range(len(ids)):
            if ids[j] == ids_min_el:
                ids_min_el_coord = j
    
        ids_used_coords.append(ids_min_el_coord)

    # сортируем список salary по возрастанию
    for k in range(len(salary)):
        for m in range(len(salary)):
            if salary[k] <= salary[m]:
                salary[k], salary[m] = salary[m], salary[k]            

    # в salary переставляем элементы по id-шникам ids_used_coords

    for i in range(len(ids_used_coords)):
        sort = ids_used_coords[i]
        sals[sort] = salary[i]
    
    # упорядочиваем элементы словаря
    for k in sorted(sals.keys()):
        sorted_sal.append(sals[k])
    
    return sorted_sal