# пока нерабочий вариант - надо разобраться с переходом на новую строку
# и дописыванием нормально в текущую строку доп. слов

stroka = 'нойшвайтшайн аушвен цумгерт аус'
massiv = list(stroka)

curr_el = 0 # текущий элемент массива
words_count = 0 # количество слов в массиве

words = [] # массив слов из строки
temp_mas = [] # буферный массив

stakan = [] # итоговый массив

shirina = 12
unfilled_cells = shirina

# засчитываем первое слово, если символ строки не пробел
if len(massiv) > 0 and massiv[0] != ' ':
    words_count += 1

for i in range(len(massiv)-1):
    # пары символов "пробел + след. не пробел" считаем за слово
    if massiv[i] == ' ' and massiv[i+1] != ' ':
        words_count += 1

# запишем каждое отдельное слово как элемент массива
for j in range(len(massiv)):
    if massiv[j] != ' ':
        temp_mas.append(massiv[j])
    elif massiv[j] == ' ':
        words.append(temp_mas)
        temp_mas = []
words.append(temp_mas)

# перенос слов по строкам "стакана"
for i in range(words_count):
    temp_mas = [] # обнуляем буферный массив
    if len(words[i]) == unfilled_cells:
        for x in range(len(words[i])):
            temp_mas.append(massiv[curr_el])
            curr_el += 1
        stakan.append(temp_mas)
        
    elif len(words[i]) < unfilled_cells:
        for x in range(len(words[i])):
            temp_mas.append(massiv[curr_el])
            temp_mas.append(' ')
            curr_el += 1
            unfilled_cells -= len(words[i])-1
        stakan.append(temp_mas)
        
    elif len(words[i]) > unfilled_cells:
        stakan.append(temp_mas)
        unffilled_cells = shirina
        for x in range(len(words[i])):
            temp_mas.append(massiv[curr_el])
            temp_mas.append(' ')
            curr_el += 1
            unfilled_cells -= len(words[i])-1
        stakan.append(temp_mas)
    