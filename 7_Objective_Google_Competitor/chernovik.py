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
        