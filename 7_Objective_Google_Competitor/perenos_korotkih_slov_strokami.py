stroka = 'алеунде цум гебурстагенпляц! швайне'

count = 0 # счетчик символов в строке
shirina = 12

stakan_text = '' # строка для результатов

for i in stroka.split(): # проходим по каждому слову
    count += len(i)
    if count > shirina:  # если символов больше, чем ширина
        stakan_text += '\n' # перенос строки
        count = len(i)
    elif stakan_text != '':  # условие, чтобы не ставить
        stakan_text += ' '   # пробел перед первым словом
        count += 1
    stakan_text += i

print(stakan_text)