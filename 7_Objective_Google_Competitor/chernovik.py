shirina = 12 # задаем ширину строки
text = "ыворвлоллаушвен цумгертаус jhg" # задаем текст для обработки
rows = [] # задаем список для хранения частей текста
while text:  # до тех пор, пока в тексте есть элементы
    if len(text) <= shirina: # это на случай того, когда у нас остаток текста меньше ширины строки
        rows.append(text) # мы помещаем этот остаток текста в строку
        text = "" # и текст по сути обнуляем, чтобы у нас завершился цикл while
    else: # для всех случаев, когда остаток строки еще больше ширины
        for i in range(shirina, 0, -1):  # для i = от 11 до 0
            if text[i] == ' ': # если встречаем пробел
                rows.append(text[:i]) # в список помещаем все, что лежит перед пробелом
                text = text[i+1:] # присвоили тексту остаток    
                break # по всей ширине строки прошлись и все
            else: # если пробела не встречаем
                rows.append(text[:i]) # в строку пишем все 12 символов
                text = text[i:] # исключаем их из текста
                break
for s in rows:
    print(s)
    

#********************

shirina = 12
stroka = 'ыворвлоллаушвен hjhjkjhjkjhj цумгертаус jhg sdfs'
w_massiv = stroka.split()
rows = []
for word in range(len(w_massiv)):
    if len(w_massiv[word]) <= shirina:
        rows.append(w_massiv[word])
        
    elif len(w_massiv[word]) == shirina:
        for i in range(shirina, 0, -1):
            rows.append(w_massiv[word][:i])
            w_massiv[word] = w_massiv[word][i:]
            
    elif len(w_massiv[word]) > shirina:
        for i in range(shirina, 0, -1):
            if w_massiv[word] != ' ':
                rows.append(w_massiv[word][:i])
                w_massiv[word] = w_massiv[word][i:]
                break
            
#********************

shirina = 12
text = 'алеундецойтебурssdsdsdsdsd kjhgkj'
stroka = text.split()
rows = []
matrix = []
unfilled_cells = shirina

for word_in_stroka in range(len(stroka)):
    while stroka[word_in_stroka]:
    
        if len(stroka[word_in_stroka]) <= shirina:
            unfilled_cells = shirina
            rows = []
            for m in range(len(stroka[word_in_stroka])):
                rows.append(stroka[word_in_stroka][m])
                unfilled_cells -= 1
            matrix.append(rows)
            stroka[word_in_stroka] = ''
    
        elif len(stroka[word_in_stroka]) > shirina:
            unfilled_cells = shirina
            rows = []
            for k in range(shirina):
                rows.append(stroka[word_in_stroka][k])
                unfilled_cells -= 1
            stroka[word_in_stroka] = stroka[word_in_stroka][k+1:]
            matrix.append(rows)
        