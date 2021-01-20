import math

itog_number = 0

# def PatternUnlock(N: int, hits: int) -> str:

diag = math.sqrt(1 ** 2 + 1 ** 2) # 1.41...

sum = 7 + 2 * diag # 9.82..

rounded_sum = round(sum, 5) # округлять результат нужно до 5-ти цифр после запятой - 9.82843

print(rounded_sum) # 9.82843

# как сделать так, чтобы результат был целым числом без запятых
# print(int(round(sum, 5)*100000))

# как получить 100000
i = 10

while rounded_sum % i != 0:
    rounded_sum *= i
    i *= 10

print(i) # i = 100000

itog_number = int(round((i * sum), 0))

print(itog_number) # 982843

# далее предусмотреть исключение нолей из числа
# взять любое тестовое число, перегнать его в массив, исключая '0'
# потом этот массив преобразовать в строку

test_massiv = []
inverted_massiv = []

test_number = 10012

i = 10
el = 0

# формируем массив значений без "0"
while test_number != 0:
    el = test_number % i
    if el == 0:
        test_number = int(test_number/i)
    else:
        test_massiv.append(el)
        test_number = int(test_number/i)

# инвертируем полученный ранее массив в норм. вид
for x in range(len(test_massiv)-1, -1, -1):
    inverted_massiv.append(test_massiv[x])

# создаем строку из списка
# при добавлении эл-тов преобразуем int в str
stroka = ''.join(str(e) for e in inverted_massiv)

print(stroka)


# далее нужно прописать алгоритм расчета длины в зависимости от введенного кода
# типа свод правил продумать - как длина считается в зависимости от введенных чисел
# то есть алгоритм смотрит текущее число и следующее. и он должен понимать - как считать длину