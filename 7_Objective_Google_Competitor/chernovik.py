stroka = '1) строка разбивaется на набор 2 строк через выравнивание по заданной ширине.'

stroka_list = list(stroka)

spisok_strok = []
shirina = 12

while stroka:
    if len(stroka) <= shirina:
        spisok_strok.append(stroka)
        stroka = ''
    else:
        count = 0
        for i in range(shirina, 0, -1):
            if stroka[i] == ' ':
                count += 1
                
        if count > 0:
            for i in range(shirina, 0, -1):
                if stroka[i] == ' ':
                    spisok_strok.append(stroka[:i])
                    stroka = stroka[i+1:]
                    break
        else:
            for i in range(shirina, 0, -1):
                spisok_strok.append(stroka[:i])
                stroka = stroka[i:]
                break
            
for i in range(len(spisok_strok)):
    print(spisok_strok[i])
    
digits = []    
find_this = 'строк'

for x in range(len(spisok_strok)):
    if find_this in spisok_strok[x] and len(find_this) == len(spisok_strok[x]):
        digits.append(1)
    elif (' ' + find_this + ' ') in spisok_strok[x]:
        digits.append(1)
    elif find_this[0] == spisok_strok[x][0] and (find_this + ' ') in spisok_strok[x]:
        digits.append(1)
    elif find_this[len(find_this)-1] == spisok_strok[x][len(spisok_strok[x])-1] and (' ' + find_this) in spisok_strok[x]:
        digits.append(1)
    else:
        digits.append(0)
        
print(digits)