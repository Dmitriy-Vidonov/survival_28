salary = [20000, 100000, 70000, 10000, 90000]
ids = [100, 50, 1, 1024, 200]

ids_min_el_coord = 0
salary_min_el_coord = 0

j = 0
ids_min_el = ids[j]
salary_min_el = salary[j]

# находим минимальный элемент в ids
for i in range(len(ids)):
    for j in range(len(ids)):
        if ids[i] <= ids_min_el:
            ids_min_el = ids[i]

print('ids_min_el =', ids_min_el)

# получаем координаты минимального элемента в ids
for i in range(len(ids)):
    if ids[i] == ids_min_el:
        ids_min_el_coord = i

print('ids_min_el_coord =', ids_min_el_coord)


# находим минимальный элемент в salary 
for i in range(len(salary)):
    for j in range(len(salary)):
        if salary[i] <= salary_min_el:
            salary_min_el = salary[i]

print('salary_min_el =', salary_min_el)

# получаем координаты минимального элемента в salary
for i in range(len(salary)):
    if salary[i] == salary_min_el:
        salary_min_el_coord = i

print('salary_min_el_coord =', salary_min_el_coord)