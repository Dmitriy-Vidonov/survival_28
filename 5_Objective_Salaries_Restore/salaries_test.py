salary = [20000, 100000, 70000, 10000, 90000]
ids = [100, 50, 1, 1024, 200]

salary_used_els = []
salary_used_coords = []

ids_used_els = []
ids_used_coords = []

ids_min_el_coord = 0
salary_min_el_coord = 0

j = 0
ids_min_el = ids[j]
salary_min_el = salary[j]

for x in range(len(ids)):

    # находим минимальный элемент в ids
    for i in range(len(ids)):
        for j in range(len(ids)):
            if ids[i] <= ids_min_el and ids_min_el not in ids_used_els:
                ids_min_el = ids[i]

    print('ids_min_el =', ids_min_el)

    # получаем координаты минимального элемента в ids
    for i in range(len(ids)):
        if ids[i] == ids_min_el and ids_min_el not in ids_used_els:
            ids_min_el_coord = i

    print('ids_min_el_coord =', ids_min_el_coord)


#############################################


    # находим минимальный элемент в salary 
    for i in range(len(salary)):
        for j in range(len(salary)):
            if salary[i] <= salary_min_el and salary_min_el not in salary_used_els:
                salary_min_el = salary[i]

    print('salary_min_el =', salary_min_el)

    # получаем координаты минимального элемента в salary
    for i in range(len(salary)):
        if salary[i] == salary_min_el and salary_min_el not in salary_used_els:
            salary_min_el_coord = i

    print('salary_min_el_coord =', salary_min_el_coord)


    # в salary ставим минимальный элемент по адресу, который равен адресу минимального элемента в ids
    salary[salary_min_el_coord], salary[ids_min_el_coord] = salary[ids_min_el_coord], salary[salary_min_el_coord]

    salary_used_els.append(salary_min_el)
    salary_used_coords.append(salary_min_el_coord)

    ids_used_els.append(ids_min_el)
    ids_used_coords.append(ids_min_el_coord)

    print('salary =', salary)

    print('salary_used_els =', salary_used_els)
    print('salary_used_coords =', salary_used_coords)

    print('ids_used_els =', ids_used_els)
    print('ids_used_coords =', ids_used_coords)

# выяснить, как сделать так, чтобы использованные элементы исключались из работы