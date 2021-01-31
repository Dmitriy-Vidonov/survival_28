stroka = 'аушвен цумгерт нойшвайтшайн аус'
massiv = list(stroka)

curr_el = 0 # текущий элемент массива

temp_mas = [] # буферный массив
stakan = [] # итоговый массив

shirina = 12

# 1 считаем длину текущего слова
curr_word_len = 0

# вычислили длину текущего слова
while massiv[curr_el] != ' ':
    curr_el += 1
    curr_word_len += 1

unfilled_cells = 0 # число свободных ячеек

# заполнили строку словом во всю ширину
curr_letter = 0

unfilled_cells = shirina

if curr_word_len == shirina:
    temp_mas = []
    for k in range(shirina):
        temp_mas.append(massiv[curr_letter])
        curr_letter += 1
    stakan.append(temp_mas)
  
# если текущее слово короче ширины
elif curr_word_len < shirina and curr_word_len <= unfilled_cells:
    temp_mas = []
    for i in range(curr_word_len):
        if massiv[curr_letter] != ' ':
            temp_mas.append(massiv[curr_letter])
            curr_letter += 1
            unfilled_cells -= 1
    stakan.append(temp_mas)

print(stakan)