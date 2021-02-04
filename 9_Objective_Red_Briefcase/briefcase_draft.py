import math

a = []
# b = []

curr_el = 0

strok_mas = []
shifr = []

stroka_default = 'отдай мою кроличью лапку'

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

print(shifr)