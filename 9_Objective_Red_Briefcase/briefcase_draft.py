import math

a = []
curr_el = 0
strok_mas = []
shifr = []
final_stroka = ''
temp_spisok = [] # временный список для формирования матрицы перед преобразованием
count = 0
itog_massiv = []

stroka_default = 'отдай мою кроличью лапку ушлепошный' #кроличью лапку плешивая псина'

print(stroka_default)

stroka = stroka_default.replace(' ', '') #убираем пробелы из строки

N = len(stroka) # длина строки - 21

koren = math.sqrt(N) # квадратный корень - 4.58

rows = int(koren) # нижняя граница корня - число строк матрицы - 4
cols = math.ceil(koren) # верхняя граница корня - число столбцов матрицы - 5

# выясняем, хватит ли размеров матрицы чтобы уместить весь текст
while rows * cols < N:
    if rows < cols:
        rows += 1
    elif rows == cols:
        rows += 1
        cols += 1
    else:
        cols += 1

# добавляем в строку пробелы до ровного счета
if len(stroka) < cols * rows:
    strok_mas = list(stroka) # преобразовали строку в список   
    for x in range(cols * rows - len(stroka)):
        strok_mas.append(' ')
    stroka = ''.join(strok_mas) # преобразовали список в строку


# сформировали матрицу а[]
while stroka:
    if len(stroka) <= cols:
        a.append(stroka)
        stroka = ''
    else:
        for i in range(cols, 0, -1):
            a.append(stroka[:i])
            stroka = stroka[i:]
            break

# выводим матрицу на экран
for x in range(len(a)): # главный цикл по числу строк - числу элементов массива а
    print()
    for y in range(len(a[x])): # смотрим длину 0, 1, 2 -ого элементов массива а. длины строк. оно же - число столбцов
        print('', a[x][y], end = '')
print()

# выдаем зашифрованный результат
for i in range(cols):
    for j in range(rows):
        if a[j][i] != ' ': shifr.append(a[j][i])
        else: continue
    if i < cols - 1:
        shifr.append(' ') # выводить до cols - 1

final_stroka = ''.join(shifr)
print(final_stroka) # выводим именно строку


# ***************** decrypting омоюу толл дюиа акчп йрьк *****************ооипей тючкп дкьуо арюуш йолшн млалы

final_stroka = 'омоюу толл дюиа акчп йрьк'

working_stroka = final_stroka.replace(' ', '') # убрали пробелы

N = len(working_stroka) # узнали длину строки

koren = math.sqrt(N) # квадратный корень - 4.58

rows = int(koren) # нижняя граница корня - число строк матрицы - 4
cols = math.ceil(koren) # верхняя граница корня - число столбцов матрицы - 5

# выясняем, хватит ли размеров матрицы чтобы уместить весь текст
while rows * cols < N:
    if rows < cols:
        rows += 1
    elif rows == cols:
        rows += 1
        cols += 1
    else:
        cols += 1

a = []

# распределили строку на строчки в списке
while final_stroka:
    if len(final_stroka) <= cols:
        a.append(final_stroka)
        final_stroka = ''
    else:
         for i in range(cols, 0, -1):
            a.append(final_stroka[:i])
            final_stroka = final_stroka[i:]
            break

for x in range(len(a)):
    count = 0
    for y in range(len(a[x])):
        if a[x][y] == ' ':
            count += 1
    if count > 0: # на тот случай, если в строке прбелы были
        a[x] = a[x].replace(' ', '') # убираем из строки пробелы
        temp_spisok = list(a[x]) # преобразование в список
        temp_spisok.append(' ') # добавление к списку пробела
        a[x] = ''.join(temp_spisok) # перевод снова в строку
    else:
        continue

print(a)

cols = len(a[0])
rows = len(a)

for x in range(cols):
    for y in range(rows):
        itog_massiv.append(a[y][x]) 

final = ''.join(itog_massiv)

print(final)