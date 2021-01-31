# возвращаем длину слова
def word_len(words):
    return len(words)
    
stroka = 'алеунде цум гебурстагенпляц!'
words = stroka.split() # преобразуем строку в массив слов
lens = map(word_len, words) # возвращаем длину каждого слова из списка слов
print(list(lens))

last_probel_position = stroka.rindex(' ') # последнее положение пробела в строке - только для строк
print(last_probel_position)