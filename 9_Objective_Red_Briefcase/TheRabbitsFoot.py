import math

def TheRabbitsFoot(s: str, encode: bool) -> str:

    a = []
    curr_el = 0
    strok_mas = []
    shifr = []
    final_stroka = ''
    temp_spisok = []
    count = 0
    itog_massiv = []

    if encode == True:

        stroka_default = s

        stroka = stroka_default.replace(' ', '') #убираем пробелы
        N = len(stroka) # длина строки
        koren = math.sqrt(N) # квадратный корень

        rows = int(koren) # нижняя граница корня - число строк
        cols = math.ceil(koren) # верхняя граница корня - число столбцов

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

        # выдаем зашифрованный результат
        for i in range(cols):
            for j in range(rows):
                if a[j][i] != ' ': shifr.append(a[j][i])
                else: continue
            if i < cols - 1:
                shifr.append(' ') # выводить до cols - 1

        final_stroka = ''.join(shifr)
    
        return final_stroka

    elif encode == False:

        #decrypting

        final_stroka = s

        working_stroka = final_stroka.replace(' ', '') # убрали пробелы
        N = len(working_stroka) # узнали длину строки
        koren = math.sqrt(N) # квадратный корень

        rows = int(koren) # нижняя граница корня
        cols = math.ceil(koren) # верхняя граница корня

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

        cols = len(a[0])
        rows = len(a)

        for x in range(cols):
            for y in range(rows):
                itog_massiv.append(a[y][x]) 

        final = ''.join(itog_massiv)

        return final
