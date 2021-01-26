import math

# 2 вспомогательных массива для преобразования числа
test_massiv = []
inverted_massiv = []

itog_number = 0 # число без запятых, с округлением до 5-ти знаков

matrix = [] # матрица для хранения чисел

length = 0 # переменная для хранения длины последовательности

codes = [1, 2, 3, 4, 5, 6, 7, 8, 9] # входные значения

extra_len = math.sqrt(1 ** 2 + 1 ** 2) # 1.41... - вычисление расстояния по диагонали

# сформировали матрицу matrix[]
for i in range(3):
    b = [] # на каждом шаге делаем очередной вложенный подсписок
    for j in range(3):
        b.append(0) 
    matrix.append(b)

# заполняем матрицу
matrix[0][0] = 6
matrix[0][1] = 1
matrix[0][2] = 9
matrix[1][0] = 5
matrix[1][1] = 2
matrix[1][2] = 8
matrix[2][0] = 4
matrix[2][1] = 3
matrix[2][2] = 7

# прописываем расчет путей между элементами матрицы
for i in range(len(codes)-1):
    # связи в верхней половине квадрата
    if codes[i] == 1 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 1: length += 1
    elif codes[i] == 1 and codes[i+1] == 5 or codes[i] == 5 and codes[i+1] == 1: length += extra_len
    elif codes[i] == 1 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 1: length += 1
    elif codes[i] == 1 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 1: length += extra_len
    elif codes[i] == 1 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 1: length += 1
    
    # связи в нижней половине квадрата
    elif codes[i] == 3 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 3: length += 1
    elif codes[i] == 3 and codes[i+1] == 5 or codes[i] == 5 and codes[i+1] == 3: length += extra_len
    elif codes[i] == 3 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 3: length += 1
    elif codes[i] == 3 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 3: length += extra_len
    elif codes[i] == 3 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 3: length += 1

    # связи в левой половине квадрата
    elif codes[i] == 5 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 5: length += 1
    elif codes[i] == 5 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 5: length += 1
    elif codes[i] == 5 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 5: length += 1

    # связи в правой половине квадрата
    elif codes[i] == 8 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 8: length += 1
    elif codes[i] == 8 and codes[i+1] == 2 or codes[i] == 2 and codes[i+1] == 8: length += 1
    elif codes[i] == 8 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 8: length += 1
    
    # связи от 2 по диагоналям
    elif codes[i] == 2 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 2: length += extra_len
    elif codes[i] == 2 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 2: length += extra_len
    elif codes[i] == 2 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 2: length += extra_len
    elif codes[i] == 2 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 2: length += extra_len
    
    # непрямые связи для 1
    elif codes[i] == 1 and codes[i+1] == 4 or codes[i] == 4 and codes[i+1] == 1: length += (1 + extra_len)
    elif codes[i] == 1 and codes[i+1] == 3 or codes[i] == 3 and codes[i+1] == 1: length += (1 + 1)
    elif codes[i] == 1 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 1: length += (1 + extra_len)

    # непрямые связи для 3
    elif codes[i] == 3 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 3: length += (1 + extra_len)
    elif codes[i] == 3 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 3: length += (1 + extra_len)

    # непрямые связи для 4
    elif codes[i] == 4 and codes[i+1] == 6 or codes[i] == 6 and codes[i+1] == 4: length += (1 + 1)
    elif codes[i] == 4 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 4: length += (extra_len + extra_len)
    elif codes[i] == 4 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 4: length += (1 + extra_len)
    elif codes[i] == 4 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 4: length += (1 + 1)

    # непрямые связи для 5
    elif codes[i] == 5 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 5: length += (1 + extra_len)
    elif codes[i] == 5 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 5: length += (1 + 1)
    elif codes[i] == 5 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 5: length += (1 + extra_len)

    # непрямые связи для 6
    elif codes[i] == 6 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 6: length += (1 + 1)
    elif codes[i] == 6 and codes[i+1] == 8 or codes[i] == 8 and codes[i+1] == 6: length += (1 + extra_len)
    elif codes[i] == 6 and codes[i+1] == 7 or codes[i] == 7 and codes[i+1] == 6: length += (extra_len + extra_len)
    
    # непрямые связи для 7
    elif codes[i] == 7 and codes[i+1] == 9 or codes[i] == 9 and codes[i+1] == 7: length += (1 + 1)

rounded_sum = round(length, 5) # округлять результат нужно до 5-ти цифр после запятой

i = float(10)

while rounded_sum % i != 0:
    rounded_sum *= i
    i *= 10

itog_number = int(round((i * length), 0))

# далее предусмотреть исключение нолей из числа
# взять любое тестовое число, перегнать его в массив, исключая '0'
# потом этот массив преобразовать в строку

i = 10
el = 0

# формируем массив значений без "0"
while itog_number != 0:
    el = itog_number % i
    if el == 0:
        itog_number = int(itog_number/i)
    else:
        test_massiv.append(el)
        itog_number = int(itog_number/i)

# инвертируем полученный ранее массив в норм. вид
for x in range(len(test_massiv)-1, -1, -1):
    inverted_massiv.append(test_massiv[x])

# создаем строку из списка
# при добавлении эл-тов преобразуем int в str
stroka = ''.join(str(e) for e in inverted_massiv)

print(stroka)