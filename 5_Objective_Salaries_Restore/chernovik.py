ids = [100, 50, 1, 1024, 200]

ids_used_els = []

ids_min_el = 0

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

    print('ids_min_el =', ids_min_el)
    print('ids_used_els =', ids_used_els)
    print()
    print('************')
    print()

