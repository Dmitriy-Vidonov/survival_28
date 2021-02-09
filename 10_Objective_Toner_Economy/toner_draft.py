def toner_consume(letter: str) -> int:
    toner = 0
    
    if letter == ' ':
        toner = 1
    
    return toner

sum = 0

dict = {}

stroka = 'one word two ' #(пробел) 1
letter = list(stroka) #преобразовали строку в массив символов
toner = list(map(toner_consume, letter)) #применили функцию к каждому эл-ту массива
print(toner)

for x in toner:
    sum += x
    
print('sum =', sum)