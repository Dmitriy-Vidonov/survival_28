ids = [50, 1, 1024]
salary = [20000, 100000, 90000]

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

    print('ids_min_el =', ids_min_el)
    print('ids_used_els =', ids_used_els)
    print('ids_min_el_coord =', ids_min_el_coord)
    print('ids_used_coords =', ids_used_coords)
    print()
    print('************')
    print()

# сортируем список salary по возрастанию
for k in range(len(salary)):
    for m in range(len(salary)):
        if salary[k] <= salary[m]:
            salary[k], salary[m] = salary[m], salary[k]

print('salary =', salary)            

# в salary переставляем элементы по id-шникам ids_used_coords
# сначала заполняем словарь ключами из нужных нам кординат из ids_used_coords
# и значениями из полученного списка ЗП после сортировки по возрастанию
for i in range(len(ids_used_coords)):
    sort = ids_used_coords[i]
    sals[sort] = salary[i]
    
# упорядочиваем элементы словаря по номерам ключей и заносим в итоговый массив
for k in sorted(sals.keys()):
    sorted_sal.append(sals[k])
    
print('Отсортированные ЗП -', sorted_sal)