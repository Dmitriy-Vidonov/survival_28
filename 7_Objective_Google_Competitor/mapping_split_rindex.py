# возвращаем длину слова
def word_len(words):
    return len(words)

 # маппинг   
stroka = 'алеунде цум гебурстагенпляц!'
words = stroka.split() # преобразуем строку в массив слов
lens = map(word_len, words) # возвращаем длину каждого слова из списка слов
print(list(lens))

# применение rindex для строк
last_probel_position = stroka.rindex(' ') # последнее положение пробела в строке - только для строк
print(last_probel_position)

# применение isspace
# isspace проверяет - вся ли строка состоит из whitespace символов или нет. whitespace - это пробелы, табы и пр.
# если все whitespace - возвращает true, иначе false
print(str.isspace(stroka)) # false, так как есть и обычные буквы кроме символов whitespace

# применение [:n]
stroka = 'Hello world!'
print(stroka[2:]) # пропустили 2 символа с начала            | llo world!
print(stroka[:2]) # напечатали только 2 символа сначала      | He
print(stroka[:-2]) # пропустили 2 символа в конце            | Hello worl
print(stroka[-2:]) # напечатали только 2 символа в конце     | d!
print(stroka[2:-2]) # обрезали по 2 символа с начала и конца | llo worl
