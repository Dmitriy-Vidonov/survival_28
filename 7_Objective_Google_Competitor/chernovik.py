shirina = 12
text = 'алеундецойтебурнойепляценвурст капут'
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
        

# ************

# пробую допилить добавление небольших слов в ту же строку, что уже начата

shirina = 12
text = 'алеундецойтебурнойепляценвурст капут'
for_text_len = list(text)
curr_el = 0
stroka = text.split()
rows = []
matrix = []
unfilled_cells = shirina

for word_in_stroka in range(len(stroka)):
    while stroka[word_in_stroka]:
    
        if len(stroka[word_in_stroka]) <= shirina and len(for_text_len) - curr_el > len(stroka[word_in_stroka]):
            if unfilled_cells < shirina : unfilled_cells = shirina
            rows = []
            for m in range(len(stroka[word_in_stroka])):
                rows.append(stroka[word_in_stroka][m])
                unfilled_cells -= 1
                curr_el += 1
            matrix.append(rows)
            stroka[word_in_stroka] = ''
    
        elif len(stroka[word_in_stroka]) > shirina:
            if unfilled_cells < shirina : unfilled_cells = shirina
            rows = []
            for k in range(unfilled_cells):
                rows.append(stroka[word_in_stroka][k])
                unfilled_cells -= 1
                curr_el += 1
            stroka[word_in_stroka] = stroka[word_in_stroka][k+1:]
            matrix.append(rows)