def WordSearch(len: int, s: str, subs: str): 

    spisok_strok = []
    digits = []   

    while s:
        if len(s) <= len:
            spisok_strok.append(s)
            s = ''
        else:
            for i in range(len, 0, -1):
                if s[i] == ' ':
                    spisok_strok.append(s[:i])
                    s = s[i+1:]
                    break
                elif s[i] != ' ':
                    spisok_strok.append(s[:i])
                    s = s[i:]
                    break
    
    for x in range(len(spisok_strok)):
        if spisok_strok[x].find(subs) != -1:
            digits.append(1)
        else:
            digits.append(0)
    return digits

s = '1) строка разб55555ивается на набор строк через выравнивание по заданной ширине.'
len = 12
subs = 'рок'
print(WordSearch(len, s, subs))