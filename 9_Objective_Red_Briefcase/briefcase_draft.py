import math

stroka_default = 'отдай мою кроличью лапку'

stroka = stroka_default.replace(' ', '') #убираем пробелы из строки

N = len(stroka) # длина строки

koren = math.sqrt(N) # квадратный корень - 4.58

nizh_granica = int(koren) # нижняя граница корня - число строк матрицы - 4
verh_granica = math.ceil(koren) # верхняя граница корня - число столбцов матрицы - 5
