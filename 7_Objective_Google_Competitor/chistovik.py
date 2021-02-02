def WordSearch(dlina: int, s: str, subs: str): 

    spisok_strok = []
    digits = []

    while s:
        if len(s) <= dlina:
            spisok_strok.append(s)
            s = ''
        else:
            count = 0
            for i in range(dlina, 0, -1):
                if s[i] == ' ':
                    count += 1
                
            if count > 0:
                for i in range(dlina, 0, -1):
                    if s[i] == ' ':
                        spisok_strok.append(s[:i])
                        s = s[i+1:]
                        break
            else:
                for i in range(dlina, 0, -1):
                    spisok_strok.append(s[:i])
                    s = s[i:]
                    break
    
    for x in range(len(spisok_strok)):
        if subs in spisok_strok[x] \
            and len(subs) == len(spisok_strok[x]):
            digits.append(1)
        elif (' ' + subs + ' ') in spisok_strok[x]:
            digits.append(1)
        elif subs[0] == spisok_strok[x][0] \
            and (subs + ' ') in spisok_strok[x]:
            digits.append(1)
        elif subs[len(subs)-1] == \
            spisok_strok[x][len(spisok_strok[x])-1] \
            and (' ' + subs) in spisok_strok[x]:
            digits.append(1)
        else:
            digits.append(0)
        
    return digits

#example
s = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
dlina = 12
subs = 'строк'
print(WordSearch(dlina, s, subs))