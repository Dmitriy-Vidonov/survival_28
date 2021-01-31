# применение [:n]
stroka = 'Hello world!'
print(stroka[2:]) # пропустили 2 символа с начала            | llo world!
print(stroka[:2]) # напечатали только 2 символа сначала      | He
print(stroka[:-2]) # пропустили 2 символа в конце            | Hello worl
print(stroka[-2:]) # напечатали только 2 символа в конце     | d!
print(stroka[2:-2]) # обрезали по 2 символа с начала и конца | llo worl

print()
print("**********")
print()

MAX_LENGTH = 12 # задаем ширину строки
text = "нойшвайт аушвен цумгерт аус" # задаем текст для обработки
rows = [] # задаем список для хранения частей текста
while text:  # до тех пор, пока в тексте есть элементы
    if len(text) <= MAX_LENGTH: # это на случай того, когда у нас остаток текста меньше ширины строки
        rows.append(text) # мы помещаем этот остаток текста в строку
        text = "" # и текст по сути обнуляем, чтобы у нас завершился цикл while
    else: # для всех случаев, когда остаток строки еще больше ширины
        for i in range(MAX_LENGTH + 1, 0, -1):  # для i = от 13 до 0 - идем по строке справа налево, с конца
            if str.isspace(text[i]): # если встречаем пробел
                rows.append(text[:i]) # в список помещаем все, что лежит перед пробелом
                text = text[i+1:] # из текста как бы вырезаем тот кусок, который мы вставили в массив rows
                break             # помещаем в текст то, что осталось после вычитания слова + пробела (+1)
for s in rows: # просто выводим все элементы
    print(s)

# **************

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