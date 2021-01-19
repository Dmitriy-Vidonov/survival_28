ids = [50, 1, 1024]

ids_used_els = []
ids_used_coords = []

ids_min_el = 0
ids_min_el_coord = 0

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

    print('ids_min_el =', ids_min_el)
    print('ids_used_els =', ids_used_els)
    print('ids_min_el_coord =', ids_min_el_coord)
    print('ids_used_coords =', ids_used_coords)
    print()
    print('************')
    print()

# 1 - отсортировать по возрастанию список salary
# 2 - в отсортированном salary переставить элементы по айдишкам из списка ids_used_coords