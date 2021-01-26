import math

def PatternUnlock(N: int, hits: int) -> str:

    # 2 вспомогательных массива для преобразования числа
    test_massiv = []
    inverted_massiv = []

    itog_number = 0 # число без запятых, с округлением до 5-ти знаков

    matrix = [] # матрица для хранения чисел

    length = 0 # переменная для хранения длины последовательности

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
    for i in range(len(hits)-1):
        # связи в верхней половине квадрата
        if hits[i] == 1 and hits[i+1] == 6 or hits[i] == 6 and hits[i+1] == 1: length += 1
        elif hits[i] == 1 and hits[i+1] == 5 or hits[i] == 5 and hits[i+1] == 1: length += extra_len
        elif hits[i] == 1 and hits[i+1] == 2 or hits[i] == 2 and hits[i+1] == 1: length += 1
        elif hits[i] == 1 and hits[i+1] == 8 or hits[i] == 8 and hits[i+1] == 1: length += extra_len
        elif hits[i] == 1 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 1: length += 1
    
        # связи в нижней половине квадрата
        elif hits[i] == 3 and hits[i+1] == 4 or hits[i] == 4 and hits[i+1] == 3: length += 1
        elif hits[i] == 3 and hits[i+1] == 5 or hits[i] == 5 and hits[i+1] == 3: length += extra_len
        elif hits[i] == 3 and hits[i+1] == 2 or hits[i] == 2 and hits[i+1] == 3: length += 1
        elif hits[i] == 3 and hits[i+1] == 8 or hits[i] == 8 and hits[i+1] == 3: length += extra_len
        elif hits[i] == 3 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 3: length += 1

        # связи в левой половине квадрата
        elif hits[i] == 5 and hits[i+1] == 6 or hits[i] == 6 and hits[i+1] == 5: length += 1
        elif hits[i] == 5 and hits[i+1] == 2 or hits[i] == 2 and hits[i+1] == 5: length += 1
        elif hits[i] == 5 and hits[i+1] == 4 or hits[i] == 4 and hits[i+1] == 5: length += 1

        # связи в правой половине квадрата
        elif hits[i] == 8 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 8: length += 1
        elif hits[i] == 8 and hits[i+1] == 2 or hits[i] == 2 and hits[i+1] == 8: length += 1
        elif hits[i] == 8 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 8: length += 1
    
        # связи от 2 по диагоналям
        elif hits[i] == 2 and hits[i+1] == 6 or hits[i] == 6 and hits[i+1] == 2: length += extra_len
        elif hits[i] == 2 and hits[i+1] == 4 or hits[i] == 4 and hits[i+1] == 2: length += extra_len
        elif hits[i] == 2 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 2: length += extra_len
        elif hits[i] == 2 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 2: length += extra_len
    
        # непрямые связи для 1
        elif hits[i] == 1 and hits[i+1] == 4 or hits[i] == 4 and hits[i+1] == 1: length += (1 + extra_len)
        elif hits[i] == 1 and hits[i+1] == 3 or hits[i] == 3 and hits[i+1] == 1: length += (1 + 1)
        elif hits[i] == 1 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 1: length += (1 + extra_len)

        # непрямые связи для 3
        elif hits[i] == 3 and hits[i+1] == 6 or hits[i] == 6 and hits[i+1] == 3: length += (1 + extra_len)
        elif hits[i] == 3 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 3: length += (1 + extra_len)

        # непрямые связи для 4
        elif hits[i] == 4 and hits[i+1] == 6 or hits[i] == 6 and hits[i+1] == 4: length += (1 + 1)
        elif hits[i] == 4 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 4: length += (extra_len + extra_len)
        elif hits[i] == 4 and hits[i+1] == 8 or hits[i] == 8 and hits[i+1] == 4: length += (1 + extra_len)
        elif hits[i] == 4 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 4: length += (1 + 1)

        # непрямые связи для 5
        elif hits[i] == 5 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 5: length += (1 + extra_len)
        elif hits[i] == 5 and hits[i+1] == 8 or hits[i] == 8 and hits[i+1] == 5: length += (1 + 1)
        elif hits[i] == 5 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 5: length += (1 + extra_len)

        # непрямые связи для 6
        elif hits[i] == 6 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 6: length += (1 + 1)
        elif hits[i] == 6 and hits[i+1] == 8 or hits[i] == 8 and hits[i+1] == 6: length += (1 + extra_len)
        elif hits[i] == 6 and hits[i+1] == 7 or hits[i] == 7 and hits[i+1] == 6: length += (extra_len + extra_len)
    
        # непрямые связи для 7
        elif hits[i] == 7 and hits[i+1] == 9 or hits[i] == 9 and hits[i+1] == 7: length += (1 + 1)

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

    return stroka