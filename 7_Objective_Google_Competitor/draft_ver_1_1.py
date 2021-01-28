stroka = 'аушвен буге цвойхтентаг!'
massiv = list(stroka)

print(massiv)

a = []
b = []

words_count = 0 # количество слов в массиве

# определяем число слов в массиве

# засчитываем первое слово, если символ строки не пробел
if len(massiv) > 0 and massiv[0] != ' ':
    words_count += 1

for i in range(len(massiv)-1):
    # пары символов "пробел + след. не пробел" считаем за слово
    if massiv[i] == ' ' and massiv[i+1] != ' ':
        words_count += 1
        
print('words_count =', words_count)
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

# считаем число строк в "стакане"
# 'стакан' - это наша матрица с перенесенными словами
if len(stroka) % shirina == 0:
    strok_v_mat_a = int(len(stroka) / shirina)
else:
    strok_v_mat_a = int(len(stroka) // shirina + 1)

unfilled_cells = 0
word_len = 0

# проверим сначала, корректно ли учитывается число
# незаполненных ячеек

# пример с занесением в элемент массива одного слова
mat_b = []
mat_b.append(a[0])
print('mat_b =', mat_b)
print('len(mat_b) =', len(mat_b[0]))

# заполняем целиком строку с пробелом и +1 словом и считаем число символов
dlina_stroki = 0
mat_b.append(' ')
mat_b.append(a[1])
dlina_stroki = len(mat_b[0]) + len(mat_b[1]) + len(mat_b[2])
print('mat_b =', mat_b)
print('len(mat_b) =', dlina_stroki)

mat_a.append(mat_b)
unfilled_cells = shirina - dlina_stroki # посчит. незап. яч.

print('mat_a[0] =', mat_a[0])

chto_ischem = 'аушвен'
slovo_na_poisk = list(chto_ischem)

# ищем слово в строке "стакана"
if slovo_na_poisk in mat_a[0]:
    print('нашли', slovo_na_poisk, 'в массиве')
else:
    print(slovo_na_poisk, 'не найдено в массиве')
    
# перенос большого слова в след. строку "стакана"
big_word = 'алеундецойтгебурстагенвагенпляц'
big_w_massiv = list(big_word)

# считаем - на сколько строк растянется наше слово
rows_count_in_big_w = 0

if len(big_w_massiv) % shirina == 0:
    rows_count_in_big_w = int(len(big_w_massiv) / shirina)
else:
    rows_count_in_big_w = int(len(big_w_massiv) // shirina + 1)

# вписываем большое слово в несколько строк "стакана"
mat_b = []
for i in range(len(big_w_massiv)):
    if i < shirina:
        mat_b.append(big_w_massiv[i])
    else:
        mat_a.append(mat_b)
        mat_b = []
        
