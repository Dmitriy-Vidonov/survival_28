def perenos_dlinnogo_slova(shirina: int, stroka: str):
    #shirina = 12 # задаем ширину стакана
    #stroka = 'алеундецойтгебурстагенвагенпляценкурст' # строка с нашим словом
    word = list(stroka) # массив с нашим словом
    rows = 0 # вводим переменную для подсчета числа строк, на которые
    # растянется наше слово

    a = [] # задаем основной массив, в котором будут строки, "стакан"
    b = [] # задаем буферный массив

    dlina_slova = 0 # задаем переменную для длины слова
    dlina_slova = len(word) # вычислили переменную длины

    curr_letter = 0 # задаем счетчик индексов букв в слове

    # считаем - на сколько строк растянется наше слово
    if len(word) % shirina == 0:
        rows = int(len(word) / shirina)
    else:
        rows = int(len(word) // shirina + 1)
    
    # основной цикл запускаем по числу строк для слова (3)
    for j in range(rows):
        # вспомогательный массив для заполнения b[]
        if dlina_slova // shirina > 0:
            for k in range(shirina):
                b.append(word[curr_letter])
                curr_letter += 1
            dlina_slova -= shirina
        else:
            for k in range(dlina_slova): # остаток символов в слове
                b.append(word[curr_letter])
                curr_letter += 1
        a.append(b) # помещаем в стакан очередную строку
        b = [] # обнуляем буферный массив для дальнейшей работы
    return a

# пример использования с выводом всего массива построчно
#shirina = 12 
#stroka = 'алеундецойтгебурстагенвагенпляценкурст'

#for i in range(len(perenos_dlinnogo_slova(shirina, stroka))):
#    print(perenos_dlinnogo_slova(shirina, stroka)[i])