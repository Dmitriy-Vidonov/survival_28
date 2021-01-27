stroka = 'одна проверочная строка с длинными словулечищщами'
massiv = list(stroka)

print(massiv)

a = []
b = []

count = 0 # количество слов в массиве

# определяем число слов в массиве

# засчитываем первое слово, если символ строки не пробел
if len(massiv) > 0 and massiv[0] != ' ':
    count += 1

for i in range(len(massiv)-1):
    # пары символов "пробел + след. не пробел" считаем за слово
    if massiv[i] == ' ' and massiv[i+1] != ' ':
        count += 1
        
print('count =', count)
j_count = 0
# запишем каждое отдельное слово как элемент массива
for j in range(len(massiv)):
    if massiv[j] != ' ':
        b.append(massiv[j])
    elif massiv[j] == ' ':
        a.append(b)
        b = []
a.append(b)
    
print('a =', a)

mat_a = []
mat_b = []
strok_v_mat_a = 0
shirina = 12

if len(stroka) % shirina == 0:
    strok_v_mat_a = len(stroka) / shirina
else:
    strok_v_mat_a = len(stroka) // shirina + 1

curr_el = 0
for M in range(strok_v_mat_a):
    mat_b = []
    for N in range(shirina):
        if curr_el < len(massiv):
            mat_b.append(massiv[curr_el])
            curr_el += 1
        else:
            continue
    mat_a.append(mat_b)

#print('mat_a =', mat_a)
print(len(a[0])) # число символов в первом слове строки