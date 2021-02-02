shirina = 12
text = 'алеундецойтебурнойепляценвурст капут'
text2 = 'алеунде цойт ебурной епл'
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


for i in matrix:
    print(i)
        

# ************разбивка текста просто по ширине
stroka = '1) строка разбивается на набор строк и букв'

#stroka = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'

spisok_strok = []
shirina = 12
curr_el = 0
podstroka = []
mesto_probela = 0

while curr_el <= len(stroka):
    if curr_el + shirina <= len(stroka):
        for curr_el in range (curr_el, curr_el + shirina):
            podstroka.append(stroka[curr_el])
            if str.isspace(stroka[curr_el]):
                mesto_probela = curr_el
            curr_el += 1
        spisok_strok.append(podstroka)
        podstroka=[]
    else:
        for j in range(len(stroka) - curr_el):
            podstroka.append(stroka[curr_el])
            if str.isspace(stroka[curr_el]):
                mesto_probela = curr_el
            curr_el += 1
        spisok_strok.append(podstroka)
        break
        
# *********************

stroka = '1) строка разбивadasdasdasdается на набор строк через выравнивание по заданной ширине.'

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
    if spisok_strok[x].find(find_this) != -1:
        digits.append(1)
    else:
        digits.append(0)
        
print(digits)